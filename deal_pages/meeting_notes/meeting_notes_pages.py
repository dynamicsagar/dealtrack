import time
import datetime
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.keys import Keys
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.request_revision.request_revision_pages import RequestRevisionPages
from deal_pages.release.release_pages import ReleasePages
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from selenium.webdriver.common.action_chains import ActionChains
from deal_pages.unrelease.unrelease_pages import UnReleasePages



class MeetingNotesPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deall = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.request = RequestRevisionPages(self.driver)
        self.release = ReleasePages(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.driver = driver

    add_meeting_notes_button = "//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/button[2]/span"
    temp_update_floor_button = "//button[contains(text(),'Update floors')]"
    element1 = "//tr[1]//td[7]//div[1]//img[2]"

    def VerifyMeetingNoteButton(self):
        time.sleep(2)
        self.deall.ClickBackArrow()
        time.sleep(2)
        self.deall.MoreFilterIcon()
        time.sleep(2)
        self.deall.ClickStageField()
        time.sleep(2)
        self.request.SelectBToA()
        time.sleep(2)
        self.deall.ClickApplyButton()
        time.sleep(2)
        for i in range(6):
            if self.isElementDisplayed(self.add_meeting_notes_button) == False:
                self.unrelease.ClickMenuIcon()
                time.sleep(2)
                self.deall.MoreFilterIcon()
                time.sleep(2)
                self.deall.ClickApplyButton()
            else:
                break
        self.elementPresenceCheck(self.add_meeting_notes_button, byType='xpath')


    enter_meeting_notes = "//textarea[@placeholder='Enter text here']"
    enter_meeting_date = "//input[@id='regionalCommitteeMeetingDate']"
    enter_time = ".sc-1b2vuwt-0"


    def EnterMeetingNote(self, text):
        self.elementClick(self.enter_meeting_notes)
        time.sleep(2)
        self.sendKeys(text, self.enter_meeting_notes)

    def EnterMeetingDate(self, a):
        self.elementClick(self.enter_meeting_date)
        time.sleep(2)
        base = datetime.datetime.now()
        a = (base + datetime.timedelta())
        a = (a.strftime("%m/%d/%Y"))
        self.log.info(a)
        self.sendKeys(a, self.enter_meeting_date)

    def EnterTime(self, tt):
        time.sleep(2)
        self.sendKeys(tt, self.enter_time, locatorType='css')

    def PressArrowKey(self, value):
        self.sendKeys(value, self.enter_time, locatorType='css')

    def AddMeetingNote(self):
        time.sleep(2)
        self.elementClick(self.add_meeting_notes_button)
        self.EnterValueInMeetingNotesModalBox()

    def EnterValueInMeetingNotesModalBox(self):
        time.sleep(2)
        text = 'This is automatic meeting notes'
        self.EnterMeetingNote(text)
        time.sleep(2)
        base = datetime.datetime.now()
        a = (base + datetime.timedelta())
        a = (a.strftime("%m/%d/%Y"))
        self.log.info(a)
        self.EnterMeetingDate(a)
        time.sleep(2)
        tt = "1212PM"
        self.elementClick(self.enter_time, locatorType='css')
        self.PressArrowKey(Keys.ARROW_LEFT)
        self.PressArrowKey(Keys.ARROW_LEFT)
        self.EnterTime(tt)
        time.sleep(2)
        self.release.ClickSaveButton()


    click_meeting_notes_from_note_section = ".sc-1nmm7de-0 svg"
    click_added_meeting_note = "//span[contains(text(),'B to A release')]"
    scroll_to_notes = "//span[contains(text(),'Notes')]"


    def VerifyAddedMeetingNotesOnNotesSection(self):
        time.sleep(2)
        self.innerScroll(self.scroll_to_notes)
        time.sleep(2)
        self.elementPresenceCheck(self.click_added_meeting_note, byType='xpath')

    select_c = "//div[5]/div/div/div[2]/div[4]/div/img"

    def VerifyMeetingNotesButtonFromCtoB(self):
        time.sleep(2)
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
            if self.isElementDisplayed(self.temp_update_floor_button) == True:
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
        time.sleep(2)
        self.elementPresenceCheck(self.add_meeting_notes_button, byType='xpath')


    def EnterValueInMeetingNotesModalBoxFromCToB(self):
        time.sleep(2)
        self.AddMeetingNote()
    
    click_added_meeting_note_from_c_to_b = "//span[contains(text(),'C to B release')]"
    
    def VerifyAddedMeetingNotesOnNotesSectionFromCtoB(self):
        time.sleep(2)
        self.innerScroll(self.scroll_to_notes)
        time.sleep(2)
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
        self.innerScrollUp(self.dealdetail.click_description)
        time.sleep(2)
        self.request.ClickDealDetailPageCancelButton()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(2)
        self.release.ReleaseProcessCTOB()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(4)
        self.elementClick(self.add_meeting_notes_button)
        time.sleep(2)
        textbox = self.getElement(self.enter_meeting_notes).get_attribute('value')
        if textbox == '':
            self.log.info("empty")
            assert True
        else:
            self.log.info("not empty")
            assert False








    



















