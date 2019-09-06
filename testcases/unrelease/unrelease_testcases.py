from deal_pages.unrelease.unrelease_pages import UnReleasePages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class UnreleaseTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.unrelease = UnReleasePages(self.driver)

    def test_01VerifyUnReleaseEToD(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyUnReleaseEToD ")
        self.log.info("*#" * 20)
        self.unrelease.UnreleaseDTOE()

    def test_02VerifyUnReleaseDToC(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyUnReleaseDToC ")
        self.log.info("*#" * 20)
        self.unrelease.UnReleaseCTOD()

    def test_03VerifyUnReleaseCToB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyUnReleaseDToC ")
        self.log.info("*#" * 20)
        self.unrelease.UnReleaseBTOC()

    def test_04VerifyUnReleaseBToA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyUnReleaseBToA ")
        self.log.info("*#" * 20)
        self.unrelease.UnReleaseATOB()

    def test_05VerifyBudgetAsNewRequiredDocWhileReleasingBToA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyBudgetAsNewRequiredDocWhileReleasingBToA ")
        self.log.info("*#" * 20)
        self.unrelease.BudgetAsNewRequiredDocWhileReleasingBToA()

    def test_06BudgetAsNewRequiredDocWhileReleasingBToA_VerifyByUploadRequiredDocAndCancelTheProcess(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07BudgetAsNewRequiredDocWhileReleasingBToA_VerifyByUploadRequiredDocAndCancelTheProcess ")
        self.log.info("*#" * 20)
        self.unrelease.VerifyByUploadRequiredDocAndCancelTheProcess()

    def test_07BudgetAsNewRequiredDocWhileReleasingBToA_VerifyInvalidFileUpload(self):
        self.log.info("*#" * 20)
        self.log.info(" BudgetAsNewRequiredDocWhileReleasingBToA_VerifyInvalidFileUpload ")
        self.log.info("*#" * 20)
        self.unrelease.BudgetAsNewRequiredDocWhileReleasingBToA_VerifyInvalidFileUpload()

    def test_08VerifyLeaseTextOnPopUp(self):
        self.log.info("*#" * 20)
        self.log.info(" Lease document validation - VerifyLeaseTextOnPopUp ")
        self.log.info("*#" * 20)
        self.unrelease.VerifyLeaseTextOnPopUp()

    def test_09VerifyLeaseAttachementByClickingLeaseDocument(self):
        self.log.info("*#" * 20)
        self.log.info(" est_09VerifyLeaseAttachementByClickingLeaseDocument ")
        self.log.info("*#" * 20)
        self.unrelease.VerifyLeaseAttachementByClickingLeaseDocument()

    def test_10VerifyGlobalApproverNotExistOnCtoBDeals(self):
        self.log.info("*#" * 20)
        self.log.info(" test_10VerifyGlobalApproverNotExistOnCtoBDeals ")
        self.log.info("*#" * 20)
        self.unrelease.VerifyGlobalApproverNotExistOnCtoBDeals()



