import time
import datetime
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.meeting_notes.meeting_notes_pages import MeetingNotesPages


class ComparablePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.meeting = MeetingNotesPages(self.driver)
        self.driver = driver


    # User sees comparables in stages C, B, A

    '''
    
    Preconditions

    User is logged in
    User is in stage C, B or A
    Steps
    
    Look at deal details page below financials
    Expected Result
    
    There should be a Comparables component
 
    
    '''

    click_comparable = "//a[contains(text(),'Comparables')]"
    compare_this_deal_to_text = "//span[contains(text(),'Compare this deal to')]"

    def VerifyComparabaleInC(self):
        time.sleep(2)
        self.deal.ClickBackArrow()
        time.sleep(2)
        self.unrelease.GlobalFilterSelection()
        time.sleep(2)
        self.elementClick(self.meeting.select_c)
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(4)
        self.elementClick(self.click_comparable)
        time.sleep(2)
        self.elementPresenceCheck(self.compare_this_deal_to_text, byType='xpath')


    select_b = "//div[5]/div/div/div[2]/div[6]/div/img"

    def SelectB(self):
        self.elementClick(self.select_b)

    def VerifyComparableSectionInB(self):
        time.sleep(2)
        self.unrelease.GlobalFilterSelection()
        time.sleep(2)
        self.SelectB()
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(4)
        self.elementClick(self.click_comparable)
        time.sleep(2)
        self.elementPresenceCheck(self.compare_this_deal_to_text, byType='xpath')


    select_a = "//div[5]/div/div/div[2]/div[8]/div/img"

    def SelectA(self):
        self.elementClick(self.select_a)

    def VerifyComparableSectionInA(self):
        time.sleep(2)
        self.unrelease.GlobalFilterSelection()
        time.sleep(2)
        self.SelectA()
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.elementClick(self.click_comparable)
        time.sleep(2)
        self.elementPresenceCheck(self.compare_this_deal_to_text, byType='xpath')


    # Comparables dropdown defaults to market average

    '''
    
    Preconditions

    User is logged in
    User is in stage C, B or A
    Steps
    
    Look at comparables section
    Expected Result
    
    The data defaults to compare to market average
    Explanatory footnote displayed under the table explaining the weighted averages. It should say: "* Avgs weighted by desk, except for total desks, RSF, and USF"


    '''

    footnote = '''//*[@id="comparables"]/span[3]'''

    def ComparablesDropdownDefaultsToMarketAverage(self):
        time.sleep(2)
        self.elementPresenceCheck(self.footnote, byType='xpath')

    drop_down_list = '''//select[@name='comparables--name']'''
    default_text = "//option[@value='Pipeline average']"

    def DefaultTextDropdown(self):
        time.sleep(2)
        text = self.getText(self.default_text)
        original_text = "Pipeline average"
        self.verifyTextContains(actualText=text, expectedText=original_text)

    def CheckValueInDropDown(self):
        time.sleep(2)
        count = self.getText(self.drop_down_list)
        count = count.split()
        self.log.info(len(count))











