import copy

import pytest
import sys

from awspricing.offers import EC2Offer

from tests.data.ebs_offer import (
    BASIC_EBS_OFFER_SKU,
    BASIC_IOPS_OFFER_SKU,
    BASIC_EBS_OFFER_DATA
)

class TestEBSOffer(object):

    @pytest.fixture(name='ebs_offer')
    def ebs_offer(self):
        offer = EC2Offer(BASIC_EBS_OFFER_DATA)
        return offer

    def test_ebs_offer(self, ebs_offer):
        assert ebs_offer.ebs_volume('gp2', region='us-east-1') == .1

    def test_ebs_iops_offer(self, ebs_offer):
        assert ebs_offer.ebs_iops(region='us-east-1') == 0.065
