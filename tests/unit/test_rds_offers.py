from awspricing.offers import RDSOffer

import pytest

from tests.data.rds_offer import BASIC_RDS_OFFER_DATA, BASIC_RDS_W_EDITION_SKU, BASIC_RDS_WO_EDITION_SKU


@pytest.fixture()
def offer():
    return RDSOffer(BASIC_RDS_OFFER_DATA)


class TestRDSOffer(object):
    def test_search_skus_w_edition_attributes(self, offer):
        assert offer.search_skus(
            instance_type='db.m4.large',
            database_engine='Oracle',
            database_edition='Standard One',
            deployment_option='Multi-AZ',
            license_model='Bring your own license',
            location='US West (Oregon)'
        ) == {BASIC_RDS_W_EDITION_SKU}

    def test_search_skus_wo_edition_attributes(self, offer):
        assert offer.search_skus(
            instance_type='db.m4.large',
            database_engine='MariaDB',
            deployment_option='Single-AZ',
            license_model='License included',
            location='Asia Pacific (Tokyo)'
        ) == {BASIC_RDS_WO_EDITION_SKU}

    def test_ondemand_hourly(self, offer):
        assert offer.ondemand_hourly(
            instance_type='db.m4.large',
            database_engine='Oracle',
            database_edition='Standard One',
            deployment_option='Multi-AZ',
            license_model='Bring your own license',
            region='us-west-2'
        ) == 0.350

    def test_reserved_hourly(self, offer):
        assert offer.reserved_hourly(
            instance_type='db.m4.large',
            database_engine='Oracle',
            database_edition='Standard One',
            deployment_option='Multi-AZ',
            license_model='Bring your own license',
            region='us-west-2',
            lease_contract_length='1yr',
            purchase_option='Partial Upfront'
        ) == 0.18597260273972605 # ( (648 / (365 * 24)) + 0.112 )

    def test_reserved_upfront(self, offer):
        assert offer.reserved_upfront(
            instance_type='db.m4.large',
            database_engine='Oracle',
            database_edition='Standard One',
            deployment_option='Multi-AZ',
            license_model='Bring your own license',
            region='us-west-2',
            lease_contract_length='1yr',
            purchase_option='All Upfront'
        ) == 1601.0
