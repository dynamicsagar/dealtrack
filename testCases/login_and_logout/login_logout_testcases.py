from deal_pages.login_and_logout.login_logout_page import login
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = login(self.driver)

    def test_01LoginToTheApp(self):
        self.log.info("*#" * 20)
        self.log.info(" Logout from Dashboard screen ")
        self.log.info("*#" * 20)
        self.lp.LoginVerification()

    def test_02logout(self):
        self.log.info("*#" * 20)
        self.log.info(" Logout from Dashboard screen ")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.LogoutValidation()





