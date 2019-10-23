from deal_pages.overview_section.overview_section_pages import OverviewSectionPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class OverviewSectionTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.overview = OverviewSectionPages(self.driver)

    def test_01OverviewSectionShouldBeBeneathThePhotoGrid(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01OverviewSectionShouldBeBeneathThePhotoGrid ")
        self.log.info("*#" * 20)
        self.overview.OverviewSectionShouldBeBeneathThePhotoGrid()

    def test_02VerifySeeMoreLinkLaunchesFloorsModal(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifySeeMoreLinkLaunchesFloorsModal ")
        self.log.info("*#" * 20)
        self.overview.SeeMoreLinkLaunchesFloorsModal()

    def test_03VerifyUserShouldBeAbleToADDFloors(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifySeeMoreLinkLaunchesFloorsModal ")
        self.log.info("*#" * 20)
        self.overview.UserShouldBeAbleToADDFloors()

    def test_04VerifyUserShouldBeAbleToUpdateFloors(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyUserShouldBeAbleToUpdateFloors ")
        self.log.info("*#" * 20)
        self.overview.UserShouldBeAbleToUpdateFloors()

    def test_05UpdatingFloorsInModalUpdatesOverviewSection(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05UpdatingFloorsInModalUpdatesOverviewSection ")
        self.log.info("*#" * 20)
        self.overview.UpdatingFloorsInModalUpdatesOverviewSection()

    def test_06AddingProductTypeInTermsTab(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06AddingProductTypeInTermsTab ")
        self.log.info("*#" * 20)
        self.overview.AddingProductTypeInTermsTab()