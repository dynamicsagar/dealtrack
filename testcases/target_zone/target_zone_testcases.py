from deal_pages.target_zone.target_zone_pages import TargetZonePages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TargetZoneTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.target = TargetZonePages(self.driver)

    def test_01VerifyMarketTierTargetZoneText(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyMarketTierTargetZoneText ")
        self.log.info("*#" * 20)
        self.target.DealDetailPageShowsWhetherADealFallsWithinTargetZone()

    def test_02VerifyTargetZoneIcon(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyTargetZoneIcon ")
        self.log.info("*#" * 20)
        self.target.VerifyTargetZoneIcon()

    def test_03VerifyTargetZoneText(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyTargetZoneText ")
        self.log.info("*#" * 20)
        self.target.VerifyTargetZoneText()