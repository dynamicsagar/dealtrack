from deal_pages.key_changes.key_changes_pages import KeyChangesPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class KeyChangeTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.key = KeyChangesPages(self.driver)

    def test_01VerifyKeyChangesChartDoesNotShowOnDealsWithNoPreviousData(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyKeyChangesChartDoesNotShowOnDealsWithNoPreviousData ")
        self.log.info("*#" * 20)
        self.key.VerifyKeyChangesChartDoesNotShowOnDealsWithNoPreviousData()

    def test_02VerifyKeyChangesChartOnlyShowsValuesThatHaveChanged(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyKeyChangesChartOnlyShowsValuesThatHaveChanged ")
        self.log.info("*#" * 20)
        self.key.VerifyKeyChangesChartOnlyShowsValuesThatHaveChanged()

    def test_03VerifyChangeColumnVariation(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyChangeColumnVariation ")
        self.log.info("*#" * 20)
        self.key.VerifyChangeColumnVariation()


