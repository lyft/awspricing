import copy

import pytest

from awspricing.offers import AWSOffer

from tests.data.ec2_offer import BASIC_EC2_OFFER_DATA, BASIC_EC2_OFFER_SKU


@pytest.fixture(name='offer')
def basic_offer():
    return AWSOffer(BASIC_EC2_OFFER_DATA)


class TestAWSOffer(object):

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
            'instanceType', 'operatingSystem', 'tenancy'
        ) == {'c4.large|Linux|Shared': BASIC_EC2_OFFER_SKU}

    def test_generate_reverse_sku_mapping_collision(self, offer):
        collision_sku = 'collision_sku'

        # Create a copy of the offer_data, as we're modifying it.
        offer._offer_data = copy.deepcopy(offer.raw)

        # Add an identical product (in terms of attributes) with a different SKU
        offer.raw['products'][collision_sku] = offer.raw['products'][BASIC_EC2_OFFER_SKU]

        assert offer._generate_reverse_sku_mapping(
            'instanceType', 'operatingSystem', 'tenancy'
        ) == {}


class TestEC2Offer(object):

    def test_search_skus_empty(self, offer):
        assert offer.search_skus() == {BASIC_EC2_OFFER_SKU}

    def test_search_skus_attributes(self, offer):
        assert offer.search_skus(
            instance_type='c4.large',
            location='US East (N. Virginia)',
        ) == {BASIC_EC2_OFFER_SKU}
