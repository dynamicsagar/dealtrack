from deal_pages.document_specific_target.document_target_pages import DocumentSpecificPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DocumentSpecificTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.document = DocumentSpecificPages(self.driver)

    def test_01VerifyAllDocumentSectionAvailable(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyAllDocumentSectionAvailable")
        self.log.info("*#" * 20)
        self.document.VerifyDocumentView()

    def test_02VerifyUploadingDocumentsOneByOne(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyUploadingDocumentsOneByOne")
        self.log.info("*#" * 20)
        self.document.UploadDocumentOneByOne()

    def test_03VerifyLockIconAfterUploadingLeaseDoc(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyLockIconAfterUploadingLeaseDoc")
        self.log.info("*#" * 20)
        self.document.VerifyLockIconAfterUploadingLeaseDocument()

    def test_04VerifyDocumentDealInStageDtoC(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyDocumentDealInStageDtoC")
        self.log.info("*#" * 20)
        self.document.DocumentDealInStageDtoC()

    def test_05VerifyDocumentDealInStageCtoB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05VerifyDocumentDealInStageCtoB")
        self.log.info("*#" * 20)
        self.document.DocumentDealInStageCtoB()

    def test_06VerifyDocumentDealInStageBtoA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06VerifyDocumentDealInStageBtoA")
        self.log.info("*#" * 20)
        self.document.DocumentDealInStageBtoA()

    def test_07VerifyRequestChangesNewlyUploadedRequiredDocIsOnThumbnail(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07VerifyRequestChangesNewlyUploadedRequiredDocIsOnThumbnail")
        self.log.info("*#" * 20)
        self.document.RequestChangesNewlyUploadedRequiredDocIsOnThumbnail()

    def test_08VerifyCancelingAReleaseRequest(self):
        self.log.info("*#" * 20)
        self.log.info(" test_08VerifyCancelingAReleaseRequest")
        self.log.info("*#" * 20)
        self.document.CancelingAReleaseRequest()