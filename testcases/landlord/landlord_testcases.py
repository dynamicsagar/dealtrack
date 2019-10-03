from deal_pages.landlord.landlord_pages import LandlordPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LandlordTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.landlord = LandlordPages(self.driver)

    def test_01VerifyDealsCanHaveMultipleLandlordsWithNoParents(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyDealsCanHaveMultipleLandlordsWithNoParents ")
        self.log.info("*#" * 20)
        self.landlord.DealsCanHaveMultipleLandlordsWithNoParents()

    def test_02VerifyLandlordsCanHaveMultipleSubsidiary(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyLandlordsCanHaveMultipleSubsidiary ")
        self.log.info("*#" * 20)
        self.landlord.LandlordsCanHaveMultipleSubsidiary()

    def test_03VerifyLandlordsCanHaveMultipleContacts(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyLandlordsCanHaveMultipleContacts ")
        self.log.info("*#" * 20)
        self.landlord.LandlordsCanHaveMultipleContacts()

    def test_04VerifyLandlordCanHaveMultipleSubContacts(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyLandlordCanHaveMultipleSubContacts ")
        self.log.info("*#" * 20)
        self.landlord.LandlordCanHaveMultipleSubContacts()
