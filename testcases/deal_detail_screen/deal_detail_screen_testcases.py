from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DealDetailTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.deal_details = DealDetailScreenPages(self.driver)

    def test_01AddDeal(self):
        self.log.info("*#" * 20)
        self.log.info(" AddDeal ")
        self.log.info("*#" * 20)
        self.deal_details.DealDetails()

    def test_02DealDetailsAddingPictures(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details adding/editing pictures ")
        self.log.info("*#" * 20)
        self.deal_details.AddPhotos()

    def test_03DealDetailsAddingDescription(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details adding/editing pictures ")
        self.log.info("*#" * 20)
        self.deal_details.Description()

    def test_07DealDetailsTeamMemberRealStateManager(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details DealMemo documents ")
        self.log.info("*#" * 20)
        self.deal_details.TeamMemberRealStateManager()

    def test_08DealDetailsTransactionManger(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details TransactionManger ")
        self.log.info("*#" * 20)
        self.deal_details.TransactionManger()

    def test_09DealDetailsSourcer(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details Sourcer ")
        self.log.info("*#" * 20)
        self.deal_details.Sourcer()

    def test_10DealDetailsRealStateAnalyst(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details RealStateAnalyst ")
        self.log.info("*#" * 20)
        self.deal_details.RealStateAnalyst()

    def test_11DealDetailsInternalCounsel(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details InternalCounsel ")
        self.log.info("*#" * 20)
        self.deal_details.InternalCounsel()

    # def test_12DealDetailsGeneralInfoTab(self):
    #     self.log.info("*#" * 20)
    #     self.log.info(" Deal details General info tab")
    #     self.log.info("*#" * 20)
    #     self.deal_details.GeneralInfoTab()

    def test_13DealDetailsTermsTab(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details Terms tab")
        self.log.info("*#" * 20)
        self.deal_details.TermsTab()

    def test_14DealDetailsPerformanceTab(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details Performance tab")
        self.log.info("*#" * 20)
        self.deal_details.PerformanceTab()

    # def test_15DealDetailsFloorsTab(self):
    #     self.log.info("*#" * 20)
    #     self.log.info(" Deal details Floors tab")
    #     self.log.info("*#" * 20)
    #     self.deal_details.FloorsTab()

    def test_17DealChangingStatus(self):
        self.log.info("*#" * 20)
        self.log.info(" DealChangingStatus to closed")
        self.log.info("*#" * 20)
        self.deal_details.DealChangingStatus()

    # def test_18LocationWalkscoreGooglePlaceAmenities(self):
    #     self.log.info("*#" * 20)
    #     self.log.info(" Location, Walkscore & Google place amenities")
    #     self.log.info("*#" * 20)
    #     self.deal_details.LocationScreenGoogle()

    def test_19ButtonORlinkToCreateDealAtExistingLocation(self):
        self.log.info("*#" * 20)
        self.log.info(" Location, Walkscore & Google place amenities")
        self.log.info("*#" * 20)
        self.deal_details.CreateDealFromExistingDeal()

    def test_20ButtonORlinkToCreateDealAtExistingLocation(self):
        self.log.info("*#" * 20)
        self.log.info(" Button/link to create deal at existing location")
        self.log.info("*#" * 20)
        self.deal_details.AddDealFromCreatedDeal()

    def test_22VerifyGrossConstructionCostOnPerformanceTab(self):
        self.log.info("*#" * 20)
        self.log.info(" test_22VerifyGrossConstructionCostOnPerformanceTab ")
        self.log.info("*#" * 20)
        self.deal_details.GrossConstructionCostONPerformanceTab()

    def test_23GrossConstructionFieldEditable(self):
        self.log.info("*#" * 20)
        self.log.info(" test_23GrossConstructionFieldEditable ")
        self.log.info("*#" * 20)
        self.deal_details.GrossConstructionFieldEditable()

    def test_24DealDetailsUploadFinancialDocs(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details Financial Documents  ")
        self.log.info("*#" * 20)
        self.deal_details.DealDetails()
        self.deal_details.FinacialDocuments()

    def test_25DealDetailsUploadTermSheetDocs(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details Term sheet documents ")
        self.log.info("*#" * 20)
        self.deal_details.TermSheetDocument()

    def test_26DealDetailsDealMemoDocs(self):
        self.log.info("*#" * 20)
        self.log.info(" Deal details DealMemo documents ")
        self.log.info("*#" * 20)
        self.deal_details.DealMemo()

    def test_27DealDetailVerifyPerformanceSectionNotEditableAfterUploadCsv(self):
        self.log.info("*#" * 20)
        self.log.info(" test_27DealDetailVerifyPerformanceSectionNotEditableAfterUploadCsv ")
        self.log.info("*#" * 20)
        self.deal_details.VerifyPerformanceSectionTabNotEditable()


