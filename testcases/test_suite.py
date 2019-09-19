import unittest
from testcases.account_tab.account_tab_testcases import AccountTabTest
from testcases.broker.broker_testcases import BrokerTest
from testcases.deal_detail_screen.deal_detail_screen_testcases import DealDetailTest
from testcases.deal_list_screen.deal_list_screen_testcases import DealListTest
from testcases.landlord.landlord_testcases import LandlordTest
from testcases.login_and_logout.login_logout_testcases import LoginTests
from testcases.release.release_testcases import ReleaseTest
from testcases.unrelease.unrelease_testcases import UnreleaseTest
from testcases.explore_tab_screen.explore_tab_screen_textcases import ExploreScreenTest
from testcases.request_revision.request_revision_testcases import RequestRevisionTest
from testcases.meeting_notes.meeting_notes_testcases import MeetingNotesTests
from testcases.photo_modal.photo_modal_testcases import PhotoModalTest
from testcases.target_zone.target_zone_testcases import TargetZoneTest

# Get all tests from the test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(BrokerTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(ReleaseTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(DealDetailTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(DealListTest)
tc6 = unittest.TestLoader().loadTestsFromTestCase(LandlordTest)
tc7 = unittest.TestLoader().loadTestsFromTestCase(AccountTabTest)
tc8 = unittest.TestLoader().loadTestsFromTestCase(UnreleaseTest)
tc9 = unittest.TestLoader().loadTestsFromTestCase(RequestRevisionTest)
tc10 = unittest.TestLoader().loadTestsFromTestCase(ExploreScreenTest)
tc11 = unittest.TestLoader().loadTestsFromTestCase(MeetingNotesTests)
tc12 = unittest.TestLoader().loadTestsFromTestCase(PhotoModalTest)
tc13 = unittest.TestLoader().loadTestsFromTestCase(TargetZoneTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc3, tc1, tc2, tc7, tc4, tc5, tc6, tc8, tc9, tc10, tc11, tc12, tc13])

unittest.TextTestRunner(verbosity=2).run(smokeTest)


