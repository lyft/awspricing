import copy

import pytest

from awspricing.offers import AWSOffer, EC2Offer
from awspricing.constants import EC2_PURCHASE_OPTION, EC2_LEASE_CONTRACT_LENGTH

from tests.data.ec2_offer import BASIC_EC2_OFFER_DATA, BASIC_EC2_OFFER_SKU, BASIC_EC2_OFFER_SKU_DATA_TRANSFER, BASIC_EC2_OFFER_SKU_DEDICATED_HOST, BASIC_EC2_OFFER_SKU_FEE, BASIC_EC2_OFFER_SKU_IP_ADDRESS, BASIC_EC2_OFFER_SKU_LOAD_BALANCER, BASIC_EC2_OFFER_SKU_LOAD_BALANCER_APPLICATION, BASIC_EC2_OFFER_SKU_NAT_GATEWAY, BASIC_EC2_OFFER_SKU_STORAGE_SNAPSHOT, BASIC_EC2_OFFER_SKU_STORAGE, BASIC_EC2_OFFER_SKU_SYSTEM_OPERATION


class TestAWSOffer(object):

    @pytest.fixture(name='offer')
    def basic_offer(self):
        return AWSOffer(BASIC_EC2_OFFER_DATA)

    def test_raw(self, offer):
        assert 'version' in offer.raw
        assert 'products' in offer.raw

    def test_pythonify_attributes(self):
        attrs = {'instance_type': 'c4.large', 'currentGeneration': 'Yes'}
        expected = {'instanceType': 'c4.large', 'currentGeneration': 'Yes'}
        assert AWSOffer._pythonify_attributes(attrs) == expected

    def test_normalize_region_not_set(self, offer):
        assert offer.default_region is None

        with pytest.raises(ValueError):
            offer._normalize_region(None)

    def test_normalize_region_default(self, offer):
        region = 'US East (N. Virginia)'
        offer.default_region = region
        assert offer._normalize_region(None) == region

    def test_normalize_region_explicit(self, offer):
        offer.default_region = 'US West (N. California)'
        region = 'US East (N. Virginia)'
        assert offer._normalize_region(region) == region

    def test_normalize_region_short(self, offer):
        assert offer._normalize_region('us-east-1') == 'US East (N. Virginia)'

    def test_generate_reverse_sku_mapping(self, offer):
        assert offer._generate_reverse_sku_mapping(
            'instanceType', 'operatingSystem', 'tenancy',
            product_family='Compute Instance'
        ) == {'c4.large|Linux|Shared': BASIC_EC2_OFFER_SKU}

    def test_generate_reverse_sku_mapping_collision(self, offer):
        collision_sku = 'collision_sku'

        # Create a copy of the offer_data, as we're modifying it.
        offer._offer_data = copy.deepcopy(offer.raw)

        # Add an identical product (in terms of attributes) with a different SKU
        offer.raw['products'][collision_sku] = offer.raw['products'][BASIC_EC2_OFFER_SKU]

        assert offer._generate_reverse_sku_mapping(
            'instanceType', 'operatingSystem', 'tenancy',
            product_family='Compute Instance'
        ) == {}


class TestEC2Offer(object):

    @pytest.fixture(name='offer')
    def basic_offer(self):
        offer = EC2Offer(BASIC_EC2_OFFER_DATA)
        offer.default_operating_system = 'Linux'
        return offer

    def test_search_skus_empty(self, offer):
        assert offer.search_skus() == {BASIC_EC2_OFFER_SKU,
                                       BASIC_EC2_OFFER_SKU_DATA_TRANSFER,
                                       BASIC_EC2_OFFER_SKU_DEDICATED_HOST,
                                       BASIC_EC2_OFFER_SKU_FEE,
                                       BASIC_EC2_OFFER_SKU_IP_ADDRESS,
                                       BASIC_EC2_OFFER_SKU_LOAD_BALANCER,
                                       BASIC_EC2_OFFER_SKU_LOAD_BALANCER_APPLICATION,
                                       BASIC_EC2_OFFER_SKU_NAT_GATEWAY,
                                       BASIC_EC2_OFFER_SKU_STORAGE_SNAPSHOT,
                                       BASIC_EC2_OFFER_SKU_STORAGE,
                                       BASIC_EC2_OFFER_SKU_SYSTEM_OPERATION}

    def test_search_skus_empty_with_family(self, offer):
        assert offer.search_skus(product_family='Compute Instance') == {BASIC_EC2_OFFER_SKU}

    def test_search_skus_attributes(self, offer):
        assert offer.search_skus(
            instance_type='c4.large',
            location='US East (N. Virginia)',
        ) == {BASIC_EC2_OFFER_SKU}

    def test_search_skus_with_wrong_productfamily_not_found(self, offer):
        assert offer.search_skus(
            instance_type='c4.large',
            location='US East (N. Virginia)',
            product_family='Storage'
        ) == set([])

    def test_search_skus_with_productfamily_found(self, offer):
        assert offer.search_skus(
            volumeType='General Purpose',
            usagetype='APS3-EBS:VolumeUsage.gp2',
            product_family='Storage'
        ) == {BASIC_EC2_OFFER_SKU_STORAGE}

    def test_reserved_hourly_no_upfront(self, offer):
        assert offer.reserved_hourly(
            'c4.large',
            region='us-east-1',
            lease_contract_length=EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR,
            purchase_option=EC2_PURCHASE_OPTION.NO_UPFRONT,
        ) == 0.063

    def test_reserved_upfront_no_upfront(self, offer):
        assert offer.reserved_upfront(
            'c4.large',
            region='us-east-1',
            lease_contract_length=EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR,
            purchase_option=EC2_PURCHASE_OPTION.NO_UPFRONT,
        ) == 0.0
