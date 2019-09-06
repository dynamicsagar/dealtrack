from deal_pages.request_revision.request_revision_pages import RequestRevisionPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DealListTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.request = RequestRevisionPages(self.driver)

    def test_01VerifyRequestRevisionButtonDToC(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyRequestRevisionButtonDToC ")
        self.log.info("*#" * 20)
        self.request.VerifyRequestRevisionButtonAvailable()

    def test_02VerifyNoApprovalButtonsAfterRequestChanges(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyNoApprovalButtonsAfterRequestChanges ")
        self.log.info("*#" * 20)
        self.request.NoApprovalButtonsAfterRequestChanges()
        
    def test_04VerifyCTAButtonShouldSayUploadDocuments(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyCTAButtonShouldSayUploadDocuments ")
        self.log.info("*#" * 20)
        self.request.CTAButtonShouldSayUploadDocuments()

    def test_05VerifyApproverSectionUpdatesToReflectRequestedChangesStatus(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05VerifyApproverSectionUpdatesToReflectRequestedChangesStatus ")
        self.log.info("*#" * 20)
        self.request.ApproverSectionUpdatesToReflectRequestedChangesStatus()

    def test_06VerifyRequestRevisionFromDToC(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06VerifyRequestRevisionFromDToC ")
        self.log.info("*#" * 20)
        self.request.VerifyRequestRevisionFromDToC()

    def test_07VerifyNoApprovalButtonsAfterRequestChangesFromCtoB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07VerifyNoApprovalButtonsAfterRequestChangesFromCtoB ")
        self.log.info("*#" * 20)
        self.request.VerifyNoApprovalButtonsAfterRequestChangesFromCtoB()

    def test_08VerifyApproverSectionUpdatesToReflectRequestedChangesStatusFromCToB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_08VerifyApproverSectionUpdatesToReflectRequestedChangesStatusFromCToB ")
        self.log.info("*#" * 20)
        self.request.ApproverSectionUpdatesToReflectRequestedChangesStatusFromCToB()

    def test_09VerifyRequestRevisionFromCtoB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_09VerifyRequestRevisionFromCtoB ")
        self.log.info("*#" * 20)
        self.request.VerifyRequestRevisionFromCToB()
        
    def test_10VerifyApprovalButtonsReturnAfterUpdatingDocumentsAfterChangesAreRequested(self):
        self.log.info("*#" * 20)
        self.log.info(" test_10VerifyApprovalButtonsReturnAfterUpdatingDocumentsAfterChangesAreRequested ")
        self.log.info("*#" * 20)
        self.request.ApprovalButtonsReturnAfterUpdatingDocumentsAfterChangesAreRequested()

    def test_11VerifyNoApprovalButtonsAfterRequestChangesFromBtoA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_11VerifyNoApprovalButtonsAfterRequestChangesFromBtoA ")
        self.log.info("*#" * 20)
        self.request.VerifyNoApprovalButtonsAfterRequestChangesFromBtoA()

    def test_12VerifyApproverSectionUpdatesToReflectRequestedChangesStatusFromBToA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_12VerifyApproverSectionUpdatesToReflectRequestedChangesStatusFromBToA ")
        self.log.info("*#" * 20)
        self.request.ApproverSectionUpdatesToReflectRequestedChangesStatusFromBToA()

    def test_13VerifyRequestRevisionFromBToA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_13VerifyRequestRevisionFromBToA ")
        self.log.info("*#" * 20)
        self.request.VerifyRequestRevisionFromBToA()

    def test_14VerifyDealRemovedFromNeedMyApprovalAfterRequestChanges(self):
        self.log.info("*#" * 20)
        self.log.info(" test_14VerifyDealRemovedFromNeedMyApprovalAfterRequestChanges ")
        self.log.info("*#" * 20)
        self.request.DealRemovedFromNeedMyApprovalAfterRequestChanges()



