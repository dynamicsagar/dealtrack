import time
import random
from selenium.webdriver.common.keys import Keys
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.release.releasing_page import ReleasePage
from deal_pages.broker.broker_pages import BrokerPages
from deal_pages.landlord.landlord_pages import LandlordPages
from utilities.util import Util


class OverviewSectionPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.release = ReleasePage(self.driver)
        self.broker = BrokerPages(self.driver)
        self.landlord = LandlordPages(self.driver)
        self.ut = Util()
        self.driver = driver


    # Overview section should be beneath the photo grid

    '''
    
    Preconditions
    User is logged into Dealtrack
    
    Steps
    Scroll to photogrid
    Look under photo grid
    
    Expected Result
    There should be a section representing a quick overview of the deal. It has the description of the deal on the left side and on the right you will see Details (Adjusted NPV, Free Rent, Product type. Below Details there is a Space section which includes USF, RSF, Desks, Floors and See more hyperlink.


    '''

    detail_tag = "//span[contains(text(),'Details')]"
    adjusted_npv_tag = "//span[contains(text(),'Adjusted NPV')]"
    space_tag = "//span[contains(text(),'Space')]"
    see_more_link = "//strong[contains(text(),'See more >')]"
    rsf = "//span[contains(text(),'RSF')]"
    usf = "//span[contains(text(),'USF')]"
    desk = "//span[contains(text(),'Desks')]"
    floors = "//span[contains(text(),'Floors')]"

    def OverviewSectionShouldBeBeneathThePhotoGrid(self):
        time.sleep(2)
        self.deal.AddNewDeal()
        time.sleep(2)
        self.elementPresenceCheck(self.detail_tag, byType='xpath')
        self.elementPresenceCheck(self.adjusted_npv_tag, byType='xpath')
        self.elementPresenceCheck(self.space_tag, byType='xpath')
        self.elementPresenceCheck(self.see_more_link, byType='xpath')
        self.elementPresenceCheck(self.rsf, byType='xpath')
        self.elementPresenceCheck(self.usf, byType='xpath')
        self.elementPresenceCheck(self.desk, byType='xpath')
        self.elementPresenceCheck(self.floors, byType='xpath')



    # "See more" link launches floors modal

    '''
    
    Preconditions
    User is logged into Dealtrack
    
    Steps
    Go to a deal in C
    Go to overview section
    Click on 'See More' text link next to "Space" heading
    
    Expected Result
    The floors edit modal should launch
    User should be able to do any floors related activities (add/remove floors, USF, RSF, Desks)
    Making changes in modal persists in overview section 

    '''

    add_floor_text = "//p[contains(text(),'Add floors')]"
    floor_count = "//div[@id='overview']//div[4]//div[1]//span[1]"
    enter_floor = "//div[@id='app']/div/div[2]/div/div/div/div[2]/div/input"
    enter_rsf = "//tr[2]//td[2]//input[1]"
    enter_usf = "//tr[2]//td[3]//input[1]"
    enter_desk = "//tr[2]//td[4]//input[1]"


    def EnterFloor(self, floor_num):
        self.elementClick(self.enter_floor)
        time.sleep(2)
        self.sendKeys(floor_num, self.enter_floor)

    def pressEnter(self, value):
        self.sendKeys(value, self.enter_floor)

    def EnterRSF(self, rsf_num):
        self.elementClick(self.enter_rsf)
        time.sleep(2)
        self.sendKeys(rsf_num, self.enter_rsf)

    def EnterUSF(self, usf_num):
        self.elementClick(self.enter_usf)
        time.sleep(2)
        self.sendKeys(usf_num, self.enter_usf)

    def EnterDesk(self, desk_num):
        self.elementClick(self.enter_desk)
        time.sleep(2)
        self.sendKeys(desk_num, self.enter_desk)


    def EnteringSecondFloorValues(self):
        floor_num = '3'
        self.EnterFloor(floor_num)
        time.sleep(2)
        self.pressEnter(Keys.ENTER)
        rsf_num = '10'
        self.EnterRSF(rsf_num)
        time.sleep(2)
        usf_num = '15'
        self.EnterUSF(usf_num)
        time.sleep(2)
        desk_num = '12'
        self.EnterDesk(desk_num)
        time.sleep(2)
        self.elementClick(self.dealdetail.click_Save_button)

    def SeeMoreLinkLaunchesFloorsModal(self):
        time.sleep(2)
        self.elementClick(self.see_more_link)
        time.sleep(2)
        self.elementPresenceCheck(self.add_floor_text, byType='xpath')

    def UserShouldBeAbleToADDFloors(self):
        time.sleep(2)
        self.dealdetail.EnteringFloorValues()
        time.sleep(2)
        text = self.getText(self.floor_count)
        expected = "1"
        self.verifyTextContains(actualText=text, expectedText=expected)

    def UserShouldBeAbleToUpdateFloors(self):
        time.sleep(2)
        self.elementClick(self.see_more_link)
        time.sleep(2)
        self.EnteringSecondFloorValues()
        time.sleep(2)
        text = self.getText(self.floor_count)
        expected = "2"
        self.verifyTextContains(actualText=text, expectedText=expected)




    # Validate TI allowance and Free Rent from proforma

    '''
    
    Preconditions
    User is logged into dealtrack
    User must have excel

    Steps
    User finds/creates a deal in D.
    Release request to C and upload a proforma (4.2 proforma, add approvers (add yourself as an approver))
    Open proforma in excel, unhide the submit to log tab
    look for Free rent from possession in months value, TI allowance value (currency)

    Expected Result
    The values in the proforma matches the values displayed in the overview section.


    '''

    # Updating floors in modal, updates overview section

    '''
    
    Preconditions
    User is logged into dealtrack
    User finds a deal with floors added
    
    Steps
    Click on the 'see more' hyperlink in overview section next to 'Space'
    Add an additional floor with RSF, USF, Desks
    Click save

    Expected Result
    Floor gets added and 'Space' in overview section is updated with the total value for RSF,USF, Desks, and Total number of floors
    
    '''


    rsf_value = "(//span[@type='3'])[4]"
    usf_value = "(//span[@type='3'])[5]"
    desk_value = "(//span[@type='3'])[6]"


    def UpdatingFloorsInModalUpdatesOverviewSection(self):
        time.sleep(2)
        rsf_text = self.getText(self.rsf_value)
        usf_text = self.getText(self.usf_value)
        desk_text = self.getText(self.desk_value)
        time.sleep(2)
        rsf_expected = "20"
        usf_expected = "30"
        desk_expected = "24"
        self.verifyTextContains(actualText=rsf_text, expectedText=rsf_expected)
        self.verifyTextContains(actualText=usf_text, expectedText=usf_expected)
        self.verifyTextContains(actualText=desk_text, expectedText=desk_expected)


    # Adding Product type in Terms tab

    '''
    
    Preconditions

    User is logged into dealtrack

    Steps

    Go to any deal
    Go to Terms tab
    Click on Product type
    Select an additional product type in multi-select dropdown
    Click save

    Expected Result

    Product types that were added persist in Terms tab and in overview section the product types are displayed with 
    comma separating them


    '''

    product_types = "(//span[@type='3'])[3]"
    click_overview = "//a[contains(text(),'Overview')]"

    def AddingProductTypeInTermsTab(self):
        time.sleep(2)
        self.elementClick(self.dealdetail.scroll_to_text)
        time.sleep(2)
        self.dealdetail.TermsTab()
        time.sleep(2)
        self.elementClick(self.click_overview)
        time.sleep(2)
        text = self.getText(self.product_types)
        expected = "Corporate"
        self.verifyTextContains(actualText=text, expectedText=expected)




















