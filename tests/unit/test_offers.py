from awspricing.offers import AWSOffer

import pytest

from tests.data.ec2_offer import BASIC_EC2_OFFER_DATA, BASIC_EC2_OFFER_SKU


@pytest.fixture()
def offer():
    return AWSOffer(BASIC_EC2_OFFER_DATA)


class TestAWSOffer(object):

    def test_raw(self, offer):
        assert 'version' in offer.raw
        assert 'products' in offer.raw

    def test_search_skus_empty(self, offer):
        assert offer.search_skus() == {BASIC_EC2_OFFER_SKU}

    def test_search_skus_attributes(self, offer):
        assert offer.search_skus(
            instance_type='c4.large',
            location='US East (N. Virginia)',
        ) == {BASIC_EC2_OFFER_SKU}

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
