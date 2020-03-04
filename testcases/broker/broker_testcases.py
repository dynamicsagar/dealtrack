from deal_pages.broker.broker_pages import BrokerPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BrokerTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.broker = BrokerPages(self.driver)

    def test_01VerifyClickingBrokerSectionOpensBrokerModal(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyClickingBrokerSectionOpensBrokerModal ")
        self.log.info("*#" * 20)
        self.broker.ClickingBrokerSectionOpensBrokerModal()

    def test_02VerifyDealDetailsPageHasEmptyBrokerSection(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyDealDetailsPageHasEmptyBrokerSection ")
        self.log.info("*#" * 20)
        self.broker.DealDetailsPageHasEmptyBrokerSection()

    # def test_03VerifyDealDetailsPageHasNotApplicableBrokerSection(self):
    #     self.log.info("*#" * 20)
    #     self.log.info(" test_03VerifyDealDetailsPageHasNotApplicableBrokerSection ")
    #     self.log.info("*#" * 20)
    #     self.broker.DealDetailsPageHasNotApplicableBrokerSection()

    def test_04VerifySubmitButtonShouldBeDisabled(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifySubmitButtonShouldBeDisabled ")
        self.log.info("*#" * 20)
        result = self.broker.SubmitButtonShouldBeDisabled()
        return result == True

    def test_05VerifyUserCanSearchAndCreateABroker(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05VerifyUserCanSearchAndCreateABroker ")
        self.log.info("*#" * 20)
        self.broker.UserCanSearchAndCreateABroker()

    def test_06VerifyUserCanEditContacts(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06VerifyUserCanEditContacts ")
        self.log.info("*#" * 20)
        self.broker.UserCanEditContacts()

    def test_07VerifyUserCanCreateANewContact(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07VerifyUserCanCreateANewContact ")
        self.log.info("*#" * 20)
        self.broker.UserCanCreateANewContact()








