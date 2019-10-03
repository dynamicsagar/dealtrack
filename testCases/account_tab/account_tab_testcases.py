from deal_pages.account_tab.account_tab_pages import AccountPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AccountTabTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.account = AccountPages(self.driver)

    def test_01VerifyAccountTab(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyAccountTab ")
        self.log.info("*#" * 20)
        self.account.VerifyAccountTab()

    def test_02VerifyEditProfilePopUp(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyEditProfilePopUp ")
        self.log.info("*#" * 20)
        self.account.EditProfile()

    def test_03VerifyEditingRegionRoleTerritory(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyEditingRegionRoleTerritory ")
        self.log.info("*#" * 20)
        self.account.SelectRegion()

    def test_04VerifyChatWithSupport(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyChatWithSupport ")
        self.log.info("*#" * 20)
        self.account.ChatSupport()

    def test_05VerifyFaq(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05VerifyFaq ")
        self.log.info("*#" * 20)
        self.account.Faq()
