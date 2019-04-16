import copy

import pytest

from awspricing.offers import AWSOffer, EC2Offer
from awspricing.constants import EC2_PURCHASE_OPTION, EC2_LEASE_CONTRACT_LENGTH

from tests.data.ec2_offer import (
    BARE_METAL_EC2_OFFER,
    BARE_METAL_EC2_SKU,
    BASIC_EC2_OFFER_DATA,
    BASIC_EC2_OFFER_SKU,
    BASIC_EC2_OFFER_MODIFIED_FORMAT
)


class TestAWSOffer(object):

    @pytest.fixture(name='offer')
    def basic_offer(self):
        return AWSOffer(BASIC_EC2_OFFER_DATA)

    @pytest.fixture
    def bare_metal_offer(self):
        return AWSOffer(BARE_METAL_EC2_OFFER)

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
            'instanceType', 'operatingSystem', 'tenancy'
        ) == {'c4.large|Linux|Shared': BASIC_EC2_OFFER_SKU}

    def test_bare_metal_included(self, bare_metal_offer):
        assert bare_metal_offer._generate_reverse_sku_mapping(
            'instanceType', 'operatingSystem', 'tenancy',
            product_families=['Compute Instance (bare metal)']
        ) == {'i3.metal|Windows|Shared': BARE_METAL_EC2_SKU}

    def test_generate_reverse_sku_mapping_collision(self, offer):
        collision_sku = 'collision_sku'

        # Create a copy of the offer_data, as we're modifying it.
        offer._offer_data = copy.deepcopy(offer.raw)

        # Add an identical product (in terms of attributes) with a different SKU
        collision_product = copy.deepcopy(offer.raw[0])
        collision_product['product']['sku'] = collision_sku
        offer.raw.append(collision_product)

        assert offer._generate_reverse_sku_mapping(
            'instanceType', 'operatingSystem', 'tenancy'
        ) == {}


class TestEC2Offer(object):

    @pytest.fixture(name='offer')
    def basic_offer(self):
        offer = EC2Offer(BASIC_EC2_OFFER_DATA)
        offer.default_operating_system = 'Linux'
        return offer

    @pytest.fixture(name='new_format_offer')
    def new_format_offer(self):
        offer = EC2Offer(BASIC_EC2_OFFER_MODIFIED_FORMAT)
        offer.default_operating_system = 'Linux'
        return offer

    def test_search_skus_empty(self, offer, new_format_offer):
        assert offer.search_skus() == {BASIC_EC2_OFFER_SKU}

    def test_search_skus_attributes(self, offer, new_format_offer):
        assert offer.search_skus(
            instance_type='c4.large',
            location='US East (N. Virginia)',
        ) == {BASIC_EC2_OFFER_SKU}

        assert new_format_offer.search_skus(
            instance_type='c4.large',
            location='US East (N. Virginia)',
        ) == {BASIC_EC2_OFFER_SKU}


    def test_reserved_hourly_no_upfront(self, offer, new_format_offer):
        assert offer.reserved_hourly(
            'c4.large',
            region='us-east-1',
            lease_contract_length=EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR,
            purchase_option=EC2_PURCHASE_OPTION.NO_UPFRONT,
        ) == 0.063

        assert new_format_offer.reserved_hourly(
            'c4.large',
            region='us-east-1',
            lease_contract_length=EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR,
            purchase_option=EC2_PURCHASE_OPTION.NO_UPFRONT,
        ) == 0.063

    def test_reserved_upfront_no_upfront(self, offer, new_format_offer):
        assert offer.reserved_upfront(
            'c4.large',
            region='us-east-1',
            lease_contract_length=EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR,
            purchase_option=EC2_PURCHASE_OPTION.NO_UPFRONT,
        ) == 0.0

        assert new_format_offer.reserved_upfront(
            'c4.large',
            region='us-east-1',
            lease_contract_length=EC2_LEASE_CONTRACT_LENGTH.ONE_YEAR,
            purchase_option=EC2_PURCHASE_OPTION.NO_UPFRONT,
        ) == 0.0
