from deal_pages.deal_list_screen.deal_list_screen_page import DealList
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DealListTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.deal = DealList(self.driver)

    def test_01AccessMyDeal(self):
        self.log.info("*#" * 20)
        self.log.info(" Access my deal filter ")
        self.log.info("*#" * 20)
        self.deal.AccessMyDealQuickFilter()

    def test_02AccessNeedMyApproval(self):
        self.log.info("*#" * 20)
        self.log.info(" Access Need my approval filter ")
        self.log.info("*#" * 20)
        self.deal.AccessNeedMyApprovalFilter()

    def test_03AccessPendingRelease(self):
        self.log.info("*#" * 20)
        self.log.info(" Access Pending Release filter ")
        self.log.info("*#" * 20)
        self.deal.AccessPendingReleaseFilter()

    def test_05AddingNewDealFunctionality(self):
        self.log.info("*#" * 20)
        self.log.info(" Adding New deal functionality ")
        self.log.info("*#" * 20)
        self.deal.AddNewDeal()

    def test_06AddingNewDealHavingDealsAlreadyAvailable(self):
        self.log.info("*#" * 20)
        self.log.info(" Adding New deal having deals already available")
        self.log.info("*#" * 20)
        self.deal.DealAlreadyAvailableText()

    # def test_07RegionFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters with Region, Territory, Market, & Landlord fields')
    #     self.log.info("*#" * 20)
    #     self.deal.RegionFilter()
    #
    # def test_08TerritoryFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters with Region, Territory, Market, & Landlord fields')
    #     self.log.info("*#" * 20)
    #     self.deal.TerritoryFilter()
    #
    # def test_09MarketFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters with Region, Territory, Market, & Landlord fields')
    #     self.log.info("*#" * 20)
    #     self.deal.MarketFilter()
    #
    # def test_10StatusFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Select status filter and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.StatusFilter()
    #
    # def test_11StageFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Select stage filter and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.StageFilter()
    #
    # def test_12ReleaseFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Select Release filter and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.ReleaseFilter()
    #
    # def test_13ProductTypeFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Select Product Type filter and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.ProductTypeFilter()
    #
    # def test_14TeamMemberFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Select Team Member filter and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.TeamMemberFilter()
    #
    # def test_15DeskFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Enter Desk filter values and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.DeskFilter()
    #
    # def test_1RSFFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Enter RSF filter values and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.RSFFilter()
    #
    # def test_17USFFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Enter USF filter values and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.USFFilter()
    #
    # def test_18PossessionFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Enter Possession filter dates and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.PosseDate()
    #
    # def test_19OpeningFieldFilter(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('More filters -- Enter Opening filter dates and verify on home page.')
    #     self.log.info("*#" * 20)
    #     self.deal.OpeningDate()
    #
    # def test_20VerifyPagination(self):
    #     self.log.info("*#" * 20)
    #     self.log.info('Pagination')
    #     self.log.info("*#" * 20)
    #     self.deal.Pagination()
























