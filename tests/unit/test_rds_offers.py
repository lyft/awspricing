from awspricing.offers import AWSOffer

import pytest

from tests.data.rds_offer import BASIC_RDS_OFFER_DATA, BASIC_RDS_W_EDITION_SKU, BASIC_RDS_WO_EDITION_SKU


@pytest.fixture()
def offer():
    return AWSOffer(BASIC_RDS_OFFER_DATA)


class TestRDSOffer(object):
    def test_search_skus_w_edition_attributes(self, offer):
        assert offer.search_skus(
            instance_type='db.m4.large',
            database_engine='Oracle',
            database_edition='Standard One',
            deployment_option='Multi-AZ',
            license_model='Bring your own license',
            location='US West (Oregon)',

        ) == {BASIC_RDS_W_EDITION_SKU}

    def test_search_skus_wo_edition_attributes(self, offer):
        assert offer.search_skus(
            instance_type='db.m4.large',
            database_engine='MariaDB',
            deployment_option='Single-AZ',
            license_model='License included',
            location='Asia Pacific (Tokyo)',

        ) == {BASIC_RDS_WO_EDITION_SKU}
