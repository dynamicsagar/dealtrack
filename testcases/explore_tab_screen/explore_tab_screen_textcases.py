from deal_pages.explore_tab_screen.explore_tab_screen_pages import ExploreScreen
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ExploreScreenTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.explore = ExploreScreen(self.driver)

    def test_01ExploreScreen(self):
        self.log.info("*#" * 20)
        self.log.info(" Explore screen -- User should redirected to Explore screen")
        self.log.info("*#" * 20)
        self.explore.ExploreNavigation()

    def test_02SearchFunctionalityOnExplore(self):
        self.log.info("*#" * 20)
        self.log.info(" Explore screen -- Search functionality on Explore")
        self.log.info("*#" * 20)
        self.explore.SearchDeal()

    def test_03AddingNewDealFromExploreTab(self):
        self.log.info("*#" * 20)
        self.log.info(" Explore screen -- Adding a new deal from Explore tab")
        self.log.info("*#" * 20)
        self.explore.AddNewDeal()

    def test_04ZoomFunctionalityOnMapView(self):
        self.log.info("*#" * 20)
        self.log.info(" Explore screen -- Zoom functionality on map-view")
        self.log.info("*#" * 20)
        self.explore.ZoomFunctionality()

    def test_05StreetViewOnMapScreen(self):
        self.log.info("*#" * 20)
        self.log.info(" Explore screen -- Street view on map screen")
        self.log.info("*#" * 20)
        self.explore.StreetView()
