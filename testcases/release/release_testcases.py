from deal_pages.release.release_pages import ReleasePages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DealListTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.release = ReleasePages(self.driver)

    def test_01VerifyReleaseEToD(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyReleaseEToD ")
        self.log.info("*#" * 20)
        self.release.ReleaseEToD()

    def test_02AddFloors(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02AddFloors ")
        self.log.info("*#" * 20)
        self.release.AddFloors()

    def test_03VerifyReleaseDToC(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyReleaseDToC ")
        self.log.info("*#" * 20)
        self.release.ReleaseDToC()

    def test_04VerifyGlobalApproversDoNotExistOnCToBDeals(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyGlobalApproversDoNotExistOnCToBDeals ")
        self.log.info("*#" * 20)
        self.release.VerifyGlobalApproversDoNotExistOnCToBDeals()

    def test_05ReleaseCToB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04ReleaseCToB ")
        self.log.info("*#" * 20)
        self.release.ReleaseCToB()

    def test_06ReleaseB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05ReleaseB ")
        self.log.info("*#" * 20)
        self.release.ReleaseMoveToB()

    def test_07ReleaseToA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06ReleaseToA ")
        self.log.info("*#" * 20)
        self.release.ReleaseToA()



