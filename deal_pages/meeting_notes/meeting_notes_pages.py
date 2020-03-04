import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.request_revision.request_revision_pages import RequestRevisionPages
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from selenium.webdriver.common.action_chains import ActionChains
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.release.releasing_page import ReleasePage


class MeetingNotesPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deall = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.request = RequestRevisionPages(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.release = ReleasePage(self.driver)
        self.driver = driver

    temp_update_floor_button = "//span[contains(text(),'Update floors')]"
    element1 = "//tr[1]//td[7]//div[1]//img[2]"

    def VerifyMeetingNoteButton(self):
        time.sleep(4)
        self.deall.ClickBackArrow()
        time.sleep(2)
        self.deall.MoreFilterIcon()
        time.sleep(2)
        self.deall.ClickStageField()
        time.sleep(2)
        self.request.SelectBToA()
        time.sleep(2)
        self.deall.ClickApplyButton()
        time.sleep(4)
        for i in range(6):
            if not self.isElementDisplayed(self.release.add_meeting_notes_button):
                self.unrelease.ClickMenuIcon()
                time.sleep(2)
                self.deall.MoreFilterIcon()
                time.sleep(2)
                self.deall.ClickApplyButton()
                time.sleep(3)
            else:
                break
        self.elementPresenceCheck(self.release.add_meeting_notes_button, byType='xpath')

    # adding meeting note by clicking on add meeting note button and then entering all the values.
    def AddMeetingNotes(self):
        self.release.AddMeetingNote()


    click_meeting_notes_from_note_section = ".sc-1nmm7de-0 svg"
    click_added_meeting_note = "//span[contains(text(),'B to A release')]"
    scroll_to_notes = "//a[contains(text(),'Notes')]"

    # verify added meeting note is showing in notes section
    def VerifyAddedMeetingNotesOnNotesSection(self):
        time.sleep(2)
        self.elementClick(self.scroll_to_notes)
        time.sleep(4)
        self.elementPresenceCheck(self.click_added_meeting_note, byType='xpath')

    select_c = "//div[5]/div/div/div[2]/div[4]/div/img"


    # add meeting notes from c to b process
    def VerifyMeetingNotesButtonFromCtoB(self):
        time.sleep(4)
        self.deall.MoreFilterIcon()
        time.sleep(2)
        self.elementClick(self.deall.reset_button)
        time.sleep(2)
        self.deall.ClickStageField()
        time.sleep(2)
        self.elementClick(self.select_c)
        time.sleep(2)
        self.deall.ClickApplyButton()
        time.sleep(4)
        for i in range(5):
            if self.isElementDisplayed(self.temp_update_floor_button):
                element_to_hover_over = self.getElement(self.element1)
                self.log.info('element found')
                hoverover = ActionChains(self.driver).move_to_element(element_to_hover_over).click().perform()
                self.log.info('element clicked')
                self.dealdetail.EnteringFloorValues()
                time.sleep(4)
                self.release.ReleaseProcessCTOB()
                time.sleep(3)
                self.dealdetail.SubmitButton()
            else:
                break
        time.sleep(5)
        self.release.ReleaseProcessCTOB()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(4)
        if self.isElementDisplayed(self.temp_update_floor_button):
            self.elementClick(self.temp_update_floor_button)
            time.sleep(2)
            self.dealdetail.EnteringFloorValues()
            time.sleep(4)
        self.elementPresenceCheck(self.release.add_meeting_notes_button, byType='xpath')


    def EnterValueInMeetingNotesModalBoxFromCToB(self):
        time.sleep(2)
        self.release.AddMeetingNote()
    
    click_added_meeting_note_from_c_to_b = "//span[contains(text(),'C to B release')]"
    
    def VerifyAddedMeetingNotesOnNotesSectionFromCtoB(self):
        time.sleep(2)
        self.elementClick(self.scroll_to_notes)
        time.sleep(4)
        self.elementPresenceCheck(self.click_added_meeting_note_from_c_to_b, byType='xpath')


    '''
    To verify the ticket we have to scroll the screen to top and then click on cancel button
    Steps:
    1. Scroll to top
    2. Click cancel button
    3. Click submit button
    4. Full release process 
    5. Click add meeting note button
    
    Expected:
    Verify meeting note modal box should be empty.
    
    '''

    def PreviousMeetingNoteIsDisplayedAndEditableWhenReleaseIsCancelled(self):
        time.sleep(2)
        # self.innerScrollUp(self.dealdetail.click_description)
        # time.sleep(2)
        self.request.ClickDealDetailPageCancelButton()
        time.sleep(2)
        self.release.ReleaseProcessCTOB()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(4)
        if self.isElementDisplayed(self.temp_update_floor_button):
            self.elementClick(self.temp_update_floor_button)
            time.sleep(2)
            self.dealdetail.EnteringFloorValues()
            time.sleep(3)
        self.elementClick(self.release.add_meeting_notes_button)
        time.sleep(2)
        textbox = self.getElement(self.release.enter_meeting_notes).get_attribute('value')
        if textbox == '':
            self.log.info("empty")
            assert True
        else:
            self.log.info("not empty")
            assert False















