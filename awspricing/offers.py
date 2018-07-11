from collections import defaultdict
import logging

from typing import Any, Dict, List, Optional, Set, Type  # noqa

import six

from .constants import (
    REGION_SHORTS,
    EC2_LEASE_CONTRACT_LENGTH,
    EC2_OFFERING_CLASS,
    EC2_PURCHASE_OPTION,
    RDS_LEASE_CONTRACT_LENGTH,
    RDS_OFFERING_CLASS,
    RDS_PURCHASE_OPTION
)


OFFER_CLASS_MAP = {}


logger = logging.getLogger(__name__)


def implements(offer_name):
    """Decorator to keep track of offer-specific class implementations."""
    def wrapper(cls):
        OFFER_CLASS_MAP[offer_name] = cls
        return cls
    return wrapper


def get_offer_class(offer_name):  # type: (str) -> Type[AWSOffer]
    return OFFER_CLASS_MAP.get(offer_name, AWSOffer)


class AWSOffer(object):
    def __init__(self, offer_data):  # type: (Dict[str, Any]) -> None
        self._offer_data = offer_data
        self.default_region = None  # type: Optional[str]

    @property
    def raw(self):
        """The entire underlying offer data."""
        return self._offer_data

    def search_skus(self, **attributes):  # type: (**str) -> Set[str]
        """Search for all SKUs matching the given attributes.

        Note that attributes given in pythonic snake_case notation will
        automatically be converted to camelCase to match AWS pricing data
        convention.

        :return: a set of matching SKUs
        """
        attributes = self._pythonify_attributes(attributes)
        result = set()
        for sku, product in six.iteritems(self._offer_data['products']):
            product_attributes = product['attributes']
            all_match = True
            for attr_name, attr_value in six.iteritems(attributes):
                if not product_attributes.get(attr_name) == attr_value:
                    all_match = False
                    break
            if all_match:
                result.add(sku)
        return result

    @staticmethod
    def _pythonify_attributes(attributes):
        # type: (Dict[str, str]) -> Dict[str, str]
        result = {}
        for attr_name, attr_value in six.iteritems(attributes):
            if '_' in attr_name:
                attr_name = ''.join(w.capitalize() or '_'
                                    for w in attr_name.split('_'))
                attr_name = attr_name[0].lower() + attr_name[1:]
            result[attr_name] = attr_value
        return result

    def _normalize_region(self, region):  # type: (Optional[str]) -> str
        region = region or self.default_region
        if not region:
            raise ValueError("No region is set.")

        if region in REGION_SHORTS:  # Use long-name to match pricing API
            region = REGION_SHORTS[region]
        return region

    @staticmethod
    def hash_attributes(*attributes):  # type: (*str) -> str
        """Generate a hash for attributes to use in reverse mappings."""
        return '|'.join(attributes)

    def _generate_reverse_sku_mapping(self,
                                      *attribute_names,  # type: str
                                      **kwargs           # type: Dict[str, str]
                                      ):
        # type: (...) -> Dict[str, str]

        """Generate a reverse mapping from a hash of product attributes to SKU.

        Only hashes that are unique across all products will be included in the
        result; products which collide on hash will be discarded.
        """

        product_families = kwargs.get('product_families')

        result = {}  # type: Dict[str, str]

        # There are cases where the set of attributes are not unique across all
        # products and cause hash collisions. In these cases, we take note of
        # the collision and do not include these products in the mapping.
        attribute_collisions = set()

        for sku, product in six.iteritems(self._offer_data['products']):
            # Introduced for Data transfer SKU's that are not like regular EC2 offers
            try:
                if product_families and product['productFamily'] not in product_families:
                    continue
            except KeyError:
                continue
            attrs = [product['attributes'][attr]
                     for attr in attribute_names if attr in product['attributes']]
            key = self.hash_attributes(*attrs)
            if key in result:
                # There is an attribute collision, so do not include any of
                # these results in the reverse mapping.
                attribute_collisions.add(key)
                del result[key]
            elif key not in attribute_collisions:
                result[key] = sku

        logger.debug('Discarded {} products when generating reverse mapping.'
                     .format(len(attribute_collisions)))

        return result


@implements('AmazonEC2')
class EC2Offer(AWSOffer):

    HOURS_IN_YEAR = 24 * 365

    def __init__(self, *args, **kwargs):
        super(EC2Offer, self).__init__(*args, **kwargs)

        self.default_operating_system = None
        self.default_tenancy = 'Shared'
        self.default_license_model = 'No License required'
        self.default_preinstalled_software = 'NA'

        self._reverse_sku = self._generate_reverse_sku_mapping(
            'instanceType', 'operatingSystem', 'tenancy', 'licenseModel',
            'preInstalledSw', 'location',
            # Both families are queried assuming that instance names will never clash between
            # them. This should be true given metal instance naming conventions thus far (instance
            # size is 'metal').
            product_families=['Compute Instance', 'Compute Instance (bare metal)']
        )

        # Lazily-loaded cache to hold offerTermCodes within a SKU
        self._reserved_terms_to_offer_term_code = defaultdict(dict)

    def get_sku(self,
                instance_type,               # type: str
                operating_system=None,       # type: Optional[str]
                tenancy=None,                # type: Optional[str]
                license_model=None,          # type: Optional[str]
                preinstalled_software=None,  # type: Optional[str]
                region=None                  # type: Optional[str]
                ):
        # type: (...) -> str
        region = self._normalize_region(region)
        operating_system = operating_system or self.default_operating_system
        tenancy = tenancy or self.default_tenancy
        license_model = license_model or self.default_license_model
        preinstalled_software = (preinstalled_software or
                                 self.default_preinstalled_software)

        attributes = [instance_type, operating_system, tenancy, license_model,
                      preinstalled_software, region]
        if not all(attributes):
            raise ValueError("All attributes are required: {}"
                             .format(attributes))

        sku = self._reverse_sku.get(self.hash_attributes(*attributes))
        if sku is None:
            raise ValueError("Unable to lookup SKU for attributes: {}"
                             .format(attributes))
        return sku

    def ondemand_hourly(self,
                        instance_type,               # type: str
                        operating_system=None,       # type: Optional[str]
                        tenancy=None,                # type: Optional[str]
                        license_model=None,          # type: Optional[str]
                        preinstalled_software=None,  # type: Optional[str]
                        region=None,                 # type: Optional[str]
                        ):
        # type: (...) -> float
        sku = self.get_sku(
            instance_type,
            operating_system=operating_system,
            tenancy=tenancy,
            license_model=license_model,
            preinstalled_software=preinstalled_software,
            region=region
        )
        term = self._offer_data['terms']['OnDemand'][sku]
        price_dimensions = next(six.itervalues(term))['priceDimensions']
        price_dimension = next(six.itervalues(price_dimensions))
        raw_price = price_dimension['pricePerUnit']['USD']
        return float(raw_price)

    def reserved_hourly(self,
                        instance_type,                               # type: str
                        operating_system=None,                       # type: Optional[str]
                        tenancy=None,                                # type: Optional[str]
                        license_model=None,                          # type: Optional[str]
                        preinstalled_software=None,                  # type: Optional[str]
                        lease_contract_length=None,                  # type: Optional[str]
                        offering_class=EC2_OFFERING_CLASS.STANDARD,  # type: str
                        purchase_option=None,                        # type: Optional[str]
                        amortize_upfront=True,                       # type: bool
                        region=None,                                 # type: Optional[str]
                        ):
        # type: (...) -> float
        self._validate_reserved_price_args(
            lease_contract_length, offering_class, purchase_option)

        assert lease_contract_length is not None
        assert offering_class is not None
        assert purchase_option is not None

        sku = self.get_sku(
            instance_type,
            operating_system=operating_system,
            tenancy=tenancy,
            license_model=license_model,
            preinstalled_software=preinstalled_software,
            region=region,
        )

        term_attributes = [
            lease_contract_length,
            offering_class,
            purchase_option
        ]
        term = self._get_reserved_offer_term(sku, term_attributes)

        price_dimensions = term['priceDimensions'].values()
        hourly_dimension = next(d for d in price_dimensions
                                if d['unit'].lower() == 'hrs')
        upfront_dimension = next((d for d in price_dimensions
                                  if d['description'] == 'Upfront Fee'), None)

        raw_hourly = hourly_dimension['pricePerUnit']['USD']
        raw_upfront = upfront_dimension['pricePerUnit']['USD'] if upfront_dimension else 0

        hourly = float(raw_hourly)
        upfront = float(raw_upfront)

        if amortize_upfront:
            hours = self._get_hours_in_lease_contract_length(
                lease_contract_length)
            hourly += (upfront / hours)

        return hourly

    def _get_reserved_offer_term(self, sku, term_attributes):
        # type: (str, List[str]) -> Dict[str, Any]
        term_attributes_hash = self.hash_attributes(*term_attributes)
        all_terms = self._offer_data['terms']['Reserved'][sku]
        sku_terms = self._reserved_terms_to_offer_term_code[sku]
        if term_attributes_hash not in sku_terms:
            for term_sku, term in six.iteritems(all_terms):
                hashed = self._hash_reserved_term_attributes(term)
                sku_terms[hashed] = term['offerTermCode']

        code = sku_terms[term_attributes_hash]
        return all_terms['.'.join([sku, code])]

    def _hash_reserved_term_attributes(self, term):
        attrs = term['termAttributes']
        return self.hash_attributes(
            attrs['LeaseContractLength'],
            attrs['OfferingClass'],
            attrs['PurchaseOption']
        )

    @classmethod
    def _get_hours_in_lease_contract_length(cls, lease_contract_length):
        if lease_contract_length == '1yr':
            return cls.HOURS_IN_YEAR
        elif lease_contract_length == '3yr':
            return 3 * cls.HOURS_IN_YEAR
        raise ValueError("Unknown lease contract length: {}"
                         .format(lease_contract_length))

    def reserved_upfront(self,
                         instance_type,                               # type: str
                         operating_system=None,                       # type: Optional[str]
                         tenancy=None,                                # type: Optional[str]
                         license_model=None,                          # type: Optional[str]
                         preinstalled_software=None,                  # type: Optional[str]
                         lease_contract_length=None,                  # type: Optional[str]
                         offering_class=EC2_OFFERING_CLASS.STANDARD,  # type: str
                         purchase_option=None,                        # type: Optional[str]
                         region=None,                                 # type: Optional[str]
                         ):
        # type: (...) -> float
        self._validate_reserved_price_args(
            lease_contract_length, offering_class, purchase_option)

        assert lease_contract_length is not None
        assert offering_class is not None
        assert purchase_option is not None

        sku = self.get_sku(
            instance_type,
            operating_system=operating_system,
            tenancy=tenancy,
            license_model=license_model,
            preinstalled_software=preinstalled_software,
            region=region,
        )

        term_attributes = [
            lease_contract_length,
            offering_class,
            purchase_option
        ]
        term = self._get_reserved_offer_term(sku, term_attributes)

        price_dimensions = term['priceDimensions'].values()
        upfront_dimension = next((d for d in price_dimensions
                                  if d['description'] == 'Upfront Fee'), None)

        raw_upfront = upfront_dimension['pricePerUnit']['USD'] if upfront_dimension else 0
        return float(raw_upfront)

    @classmethod
    def _validate_reserved_price_args(cls,
                                      lease_contract_length,  # type: Optional[str]
                                      offering_class,         # type: Optional[str]
                                      purchase_option,        # type: Optional[str]
                                      ):
        # type: (...) -> None
        if lease_contract_length not in EC2_LEASE_CONTRACT_LENGTH.values():
            valid_options = EC2_LEASE_CONTRACT_LENGTH.values()
            raise ValueError(
                "Lease contract '{}' is invalid. Valid options are: {}"
                .format(lease_contract_length, valid_options)
            )

        if offering_class not in EC2_OFFERING_CLASS.values():
            valid_options = EC2_OFFERING_CLASS.values()
            raise ValueError(
                "Offering class '{}' is invalid. Valid options are: {}"
                .format(offering_class, valid_options)
            )

        if purchase_option not in EC2_PURCHASE_OPTION.values():
            valid_options = EC2_PURCHASE_OPTION.values()
            raise ValueError(
                "Purchase option '{}' is invalid. Valid options are: {}"
                .format(purchase_option, valid_options)
            )

        if (lease_contract_length == EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR and
                offering_class == 'convertible'):
            raise ValueError("The convertible offering class is not available "
                             "on a 1year lease.")


@implements('AmazonRDS')
class RDSOffer(AWSOffer):

    HOURS_IN_YEAR = 24 * 365

    def __init__(self, *args, **kwargs):
        super(RDSOffer, self).__init__(*args, **kwargs)

        self.default_deployment_option = 'Single-AZ'

        self._reverse_sku = self._generate_reverse_sku_mapping(
            'instanceType',
            'databaseEngine',
            'deploymentOption',
            'licenseModel',
            'location',
            'databaseEdition',
            product_families=['Database Instance']
        )

        # Lazily-loaded cache to hold offerTermCodes within a SKU
        self._reserved_terms_to_offer_term_code = defaultdict(dict)  # type: Dict[str, Dict]

    def get_sku(self,
                instance_type,               # type: str
                database_engine,             # type: str
                license_model=None,          # type: Optional[str]
                deployment_option=None,      # type: Optional[str]
                database_edition=None,       # type: Optional[str]
                region=None                  # type: Optional[str]
                ):
        region = self._normalize_region(region)
        deployment_option = deployment_option or self.default_deployment_option

        if license_model is None:
            raise ValueError("License model is required")

        attributes = [instance_type, database_engine,
                      deployment_option, license_model, region]  # type: List[str]

        if database_edition is not None:
            attributes.append(database_edition)

        if not all(attributes):
            raise ValueError("All attributes are required: {}"
                             .format(attributes))

        sku = self._reverse_sku.get(self.hash_attributes(*attributes))
        if sku is None:
            raise ValueError("Unable to lookup SKU for attributes: {}"
                             .format(attributes))
        return sku

    def ondemand_hourly(self,
                        instance_type,               # type: str
                        database_engine,             # type: str
                        license_model=None,          # type: str
                        deployment_option=None,      # type: Optional[str]
                        database_edition=None,       # type: Optional[str]
                        region=None                  # type: Optional[str]
                        ):
        # type: (...) -> float
        sku = self.get_sku(
            instance_type,
            database_engine,
            deployment_option=deployment_option,
            license_model=license_model,
            database_edition=database_edition,
            region=region
        )
        term = self._offer_data['terms']['OnDemand'][sku]
        price_dimensions = next(six.itervalues(term))['priceDimensions']
        price_dimension = next(six.itervalues(price_dimensions))
        raw_price = price_dimension['pricePerUnit']['USD']
        return float(raw_price)

    def reserved_hourly(self,
                        instance_type,               # type: str
                        database_engine,             # type: str
                        license_model=None,          # type: str
                        deployment_option=None,      # type: Optional[str]
                        lease_contract_length=None,                  # type: Optional[str]
                        offering_class=RDS_OFFERING_CLASS.STANDARD,  # type: str
                        purchase_option=None,                        # type: Optional[str]
                        amortize_upfront=True,                       # type: bool
                        database_edition=None,                       # type: Optional[str]
                        region=None,                                 # type: Optional[str]
                        ):
        # type: (...) -> float
        self._validate_reserved_price_args(
            lease_contract_length, offering_class, purchase_option)

        assert lease_contract_length is not None
        assert offering_class is not None
        assert purchase_option is not None

        sku = self.get_sku(
            instance_type,
            database_engine,
            deployment_option=deployment_option,
            license_model=license_model,
            database_edition=database_edition,
            region=region,
        )

        term_attributes = [
            lease_contract_length,
            offering_class,
            purchase_option
        ]
        term = self._get_reserved_offer_term(sku, term_attributes)

        price_dimensions = term['priceDimensions'].values()
        hourly_dimension = next(d for d in price_dimensions
                                if d['unit'].lower() == 'hrs')
        upfront_dimension = next((d for d in price_dimensions
                                  if d['description'] == 'Upfront Fee'), None)

        raw_hourly = hourly_dimension['pricePerUnit']['USD']
        raw_upfront = upfront_dimension['pricePerUnit']['USD'] if upfront_dimension else 0

        hourly = float(raw_hourly)
        upfront = float(raw_upfront)

        if amortize_upfront:
            hours = self._get_hours_in_lease_contract_length(
                lease_contract_length)
            hourly += (upfront / hours)

        return hourly

    def _get_reserved_offer_term(self, sku, term_attributes):
        # type: (str, List[str]) -> Dict[str, Any]
        term_attributes_hash = self.hash_attributes(*term_attributes)
        all_terms = self._offer_data['terms']['Reserved'][sku]
        sku_terms = self._reserved_terms_to_offer_term_code[sku]
        if term_attributes_hash not in sku_terms:
            for term_sku, term in six.iteritems(all_terms):
                hashed = self._hash_reserved_term_attributes(term)
                sku_terms[hashed] = term['offerTermCode']

        code = sku_terms[term_attributes_hash]
        return all_terms['.'.join([sku, code])]

    def _hash_reserved_term_attributes(self, term):
        attrs = term['termAttributes']
        return self.hash_attributes(
            attrs['LeaseContractLength'],
            attrs['OfferingClass'],
            attrs['PurchaseOption']
        )

    @classmethod
    def _get_hours_in_lease_contract_length(cls, lease_contract_length):
        if lease_contract_length == '1yr':
            return cls.HOURS_IN_YEAR
        elif lease_contract_length == '3yr':
            return 3 * cls.HOURS_IN_YEAR
        raise ValueError("Unknown lease contract length: {}"
                         .format(lease_contract_length))

    def reserved_upfront(self,
                         instance_type,                               # type: str
                         database_engine,                             # type: str
                         license_model=None,                          # type: str
                         deployment_option=None,                      # type: Optional[str]
                         lease_contract_length=None,                  # type: Optional[str]
                         offering_class=RDS_OFFERING_CLASS.STANDARD,  # type: str
                         purchase_option=None,                        # type: Optional[str]
                         database_edition=None,                        # type: Optional[str]
                         region=None,                                 # type: Optional[str]
                         ):
        # type: (...) -> float
        self._validate_reserved_price_args(
            lease_contract_length, offering_class, purchase_option)

        assert lease_contract_length is not None
        assert offering_class is not None
        assert purchase_option is not None

        sku = self.get_sku(
            instance_type,
            database_engine,
            deployment_option=deployment_option,
            license_model=license_model,
            database_edition=database_edition,
            region=region,
        )

        term_attributes = [
            lease_contract_length,
            offering_class,
            purchase_option
        ]
        term = self._get_reserved_offer_term(sku, term_attributes)

        price_dimensions = term['priceDimensions'].values()
        upfront_dimension = next((d for d in price_dimensions
                                  if d['description'] == 'Upfront Fee'), None)

        raw_upfront = upfront_dimension['pricePerUnit']['USD'] if upfront_dimension else 0
        return float(raw_upfront)

    @classmethod
    def _validate_reserved_price_args(cls,
                                      lease_contract_length,  # type: Optional[str]
                                      offering_class,         # type: str
                                      purchase_option,        # type: Optional[str]
                                      ):
        # type: (...) -> None
        if lease_contract_length not in RDS_LEASE_CONTRACT_LENGTH.values():
            valid_options = RDS_LEASE_CONTRACT_LENGTH.values()
            raise ValueError(
                "Lease contract '{}' is invalid. Valid options are: {}"
                .format(lease_contract_length, valid_options)
            )

        if offering_class not in RDS_OFFERING_CLASS.values():
            valid_options = RDS_OFFERING_CLASS.values()
            raise ValueError(
                "Offering class '{}' is invalid. Valid options are: {}"
                .format(offering_class, valid_options)
            )

        if purchase_option not in RDS_PURCHASE_OPTION.values():
            valid_options = RDS_PURCHASE_OPTION.values()
            raise ValueError(
                "Purchase option '{}' is invalid. Valid options are: {}"
                .format(purchase_option, valid_options)
            )
