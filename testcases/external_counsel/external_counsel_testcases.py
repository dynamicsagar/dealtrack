from deal_pages.external_counsel.external_counsel_pages import ExternalCounselPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ExternalCounselTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.external = ExternalCounselPages(self.driver)

    def test_01UserShouldSeeExternalCounselSection(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01UserShouldSeeExternalCounselSection ")
        self.log.info("*#" * 20)
        self.external.UserShouldSeeExternalCounselSection()

    def test_02VerifyExternalCounselHasEmptyState(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyExternalCounselHasEmptyState ")
        self.log.info("*#" * 20)
        self.external.ExternalCounselHasEmptyState()

    def test_03ClickingOnExternalCounselSectionLaunchesEditModal(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03ClickingOnExternalCounselSectionLaunchesEditModal ")
        self.log.info("*#" * 20)
        self.external.ClickingOnExternalCounselSectionLaunchesEditModal()


    def test_04ClickingAddExternalCounselShowsTypeahead(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04ClickingAddExternalCounselShowsTypeahead ")
        self.log.info("*#" * 20)
        self.external.ClickingAddExternalCounselShowsTypeahead()


    def test_05UserCanSearchForExistingFirms(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05UserCanSearchForExistingFirms ")
        self.log.info("*#" * 20)
        self.external.UserCanSearchForExistingFirms()

    def test_06UserCanSearchForExistingLawyerAtFirmOrAddNewLawyer(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06UserCanSearchForExistingLawyerAtFirmOrAddNewLawyer ")
        self.log.info("*#" * 20)
        self.external.UserCanSearchForExistingLawyerAtFirmOrAddNewLawyer()

    def test_07ThereCanBeMultipleLawyersAssignedToADeal(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07ThereCanBeMultipleLawyersAssignedToADeal ")
        self.log.info("*#" * 20)
        self.external.ThereCanBeMultipleLawyersAssignedToADeal()

    def test_08ExternalCounselThatHasFirmAndLawyers(self):
        self.log.info("*#" * 20)
        self.log.info(" test_08ExternalCounselThatHasFirmAndLawyers ")
        self.log.info("*#" * 20)
        self.external.ExternalCounselThatHasFirmAndLawyers()

    def test_09UserCanRemoveLawyerByClickingX(self):
        self.log.info("*#" * 20)
        self.log.info(" test_09UserCanRemoveLawyerByClickingX ")
        self.log.info("*#" * 20)
        self.external.UserCanRemoveLawyerByClickingX()

    def test_10ExternalCounselShowsOnlyLawyers(self):
        self.log.info("*#" * 20)
        self.log.info(" test_10ExternalCounselShowsOnlyLawyers ")
        self.log.info("*#" * 20)
        self.external.ExternalCounselShowsOnlyLawyers()

    def test_11WhenUserRemoveFirmUsingCrossIcon(self):
        self.log.info("*#" * 20)
        self.log.info(" test_11WhenUserRemoveFirmUsingCrossIcon ")
        self.log.info("*#" * 20)
        self.external.WhenUserRemoveFirmUsingCrossIcon()

