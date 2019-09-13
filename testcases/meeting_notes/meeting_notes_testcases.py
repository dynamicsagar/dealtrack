from deal_pages.meeting_notes.meeting_notes_pages import MeetingNotesPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MeetingNotesTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.meeting = MeetingNotesPages(self.driver)

    def test_01VerifyMeetingNoteButton(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyMeetingNoteButton ")
        self.log.info("*#" * 20)
        self.meeting.VerifyMeetingNoteButton()


    def test_02AddMeetingNotesBtoA(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02AddMeetingNotesBtoA ")
        self.log.info("*#" * 20)
        self.meeting.AddMeetingNote()


    def test_03VerifyAddedMeetingNotesOnNotesSection(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyAddedMeetingNotesOnNotesSection ")
        self.log.info("*#" * 20)
        self.meeting.VerifyAddedMeetingNotesOnNotesSection()

    def test_04VerifyMeetingNotesButtonFromCtoB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyMeetingNotesButtonFromCtoB ")
        self.log.info("*#" * 20)
        self.meeting.VerifyMeetingNotesButtonFromCtoB()

    def test_05VerifyEnterValueInMeetingNotesModalBoxFromCToB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05VerifyEnterValueInMeetingNotesModalBoxFromCToB ")
        self.log.info("*#" * 20)
        self.meeting.EnterValueInMeetingNotesModalBoxFromCToB()

    def test_06VerifyVerifyAddedMeetingNotesOnNotesSectionFromCtoB(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06VerifyVerifyAddedMeetingNotesOnNotesSectionFromCtoB ")
        self.log.info("*#" * 20)
        self.meeting.VerifyAddedMeetingNotesOnNotesSectionFromCtoB()


    def test_07VerifyPreviousMeetingNoteIsDisplayedAndEditableWhenReleaseIsCancelled(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07VerifyPreviousMeetingNoteIsDisplayedAndEditableWhenReleaseIsCancelled ")
        self.log.info("*#" * 20)
        self.meeting.PreviousMeetingNoteIsDisplayedAndEditableWhenReleaseIsCancelled()