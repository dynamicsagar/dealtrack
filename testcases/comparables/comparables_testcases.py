from deal_pages.comparables.comparables_page import ComparablePage
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ComparableTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.compare = ComparablePage(self.driver)

    def test_01VerifyComparabaleInC(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyComparabaleInC ")
        self.log.info("*#" * 20)
        self.compare.VerifyComparabaleInC()

    def test_02VerifyComparableSectionInB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyComparableSectionInB ")
        self.log.info("*#" * 20)
        self.compare.VerifyComparableSectionInB()

    def test_03VerifyComparableSectionInA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyComparableSectionInA ")
        self.log.info("*#" * 20)
        self.compare.VerifyComparableSectionInA()

    def test_04ComparablesDropdownDefaultsToMarketAverage(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04ComparablesDropdownDefaultsToMarketAverage ")
        self.log.info("*#" * 20)
        self.compare.ComparablesDropdownDefaultsToMarketAverage()

    def test_05DefaultTextDropdown(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05DefaultTextDropdown")
        self.log.info("*#" * 20)
        self.compare.DefaultTextDropdown()

    def test_06CheckValueInDropDown(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06CheckValueInDropDown")
        self.log.info("*#" * 20)
        self.compare.CheckValueInDropDown()