import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.release.release_pages import ReleasePages
from deal_pages.broker.broker_pages import BrokerPages
from utilities.util import Util


class LandlordPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.release = ReleasePages(self.driver)
        self.broker = BrokerPages(self.driver)
        self.ut = Util()
        self.driver = driver


    #  Deals can have multiple landlords with no parents

    '''
    
    Deals can have multiple landlords with no parents

    Precondition : There should be no landlords under the header yet
    
    Click edit (pencil icon) - Modal should pop up
    Modal should allow inputting multiple landlords - add landlord a, b and c with contact info but, no parents
    Press Save
    
    Expected :
    The landlord section should show all 3 landlords and they’re contact info.
     All 3 landlords should be at the same level (no children no parents)
        
    '''

    landlord_tab = "//h4[contains(text(),'Landlord')]"
    add_landlord_link = "//p[contains(.,'+ Add landlord')]"
    landlord_textbox = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div/div/input"
    save_button = "//span[contains(text(),'Save')]"
    check_element_present = "//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div[13]/div/div[2]/div/div[2]/div"

    def Verification(self):
        time.sleep(2)
        self.elementClick(self.save_button)
        time.sleep(3)
        sa = self.elementPresenceCheck(self.check_element_present, byType='xpath')
        self.log.info(sa)

    def EnterLandlord(self, landlord):
        self.elementClick(self.landlord_textbox)
        time.sleep(2)
        self.sendKeys(landlord, self.landlord_textbox)

    def RandomLandlordName(self):
        landname = 'landlord'
        name = self.ut.getUniqueName(4)
        name = landname + name
        self.EnterLandlord(name)

    def DealsCanHaveMultipleLandlordsWithNoParents(self):
        time.sleep(2)
        self.innerScroll(self.landlord_tab)
        time.sleep(2)
        self.elementClick(self.landlord_tab)
        time.sleep(2)
        for i in range(1, 4):
            self.elementClick(self.add_landlord_link)
            time.sleep(2)
            self.RandomLandlordName()
            self.broker.ClickCreateNew()
            time.sleep(2)
        self.elementClick(self.save_button)


    # Landlords can have multiple children

    '''
    
    Landlords can have multiple children

    1.Click edit (pencil icon) - Modal should pop up
    2.Add a landlord (landlord A)
    3.Add 2 landlords (B and C) with A parent
    
    Expected:
    Reexamine the landlord section of deal detail page,
    landlord A should be first with landlords B and C at the same level underneath it
    
    '''

    add_subsidiary_link = "//div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/p"
    subsidiary_company = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/input"
    click_create = ".contact-search--create-option"


    def EnterSubsidiary_company(self, subsidiaryname):
        self.elementClick(self.subsidiary_company)
        time.sleep(2)
        self.sendKeys(subsidiaryname, self.subsidiary_company)

    def RandomSubsidiary_company(self):
        subsidiaryname = 'Subsidiary'
        name = self.ut.getUniqueName(4)
        name = subsidiaryname + name
        self.EnterSubsidiary_company(name)

    def LandlordsCanHaveMultipleSubsidiary(self):
        time.sleep(2)
        self.elementClick(self.landlord_tab)
        time.sleep(2)
        for i in range(1, 4):
            x = [i]
            a = '//div[2]/div/div/div/div/div/div/div'
            c = '/div/div[2]/div/div[2]/p'
            add_subsidiary = a + str(x) + c
            time.sleep(2)
            self.elementClick(add_subsidiary)
            self.RandomSubsidiary_company()
            time.sleep(2)
            self.elementClick(self.click_create, locatorType='css')
        self.Verification()


    click_add_contact = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div/div[1]/p'''

    def LandlordsCanHaveMultipleContacts(self):
        time.sleep(3)
        self.elementClick(self.landlord_tab)
        time.sleep(2)
        for i in range(1, 4):
            x = [i]
            a = '//*[@id="app"]/div/div[2]/div/div/div[1]/div/div/div[1]/div'
            c = '/div[1]/div[2]/div/div[1]/p'
            add_contact = a + str(x) + c
            time.sleep(2)
            self.elementClick(add_contact)
            self.RandomSubsidiary_company()
            time.sleep(2)
            self.elementClick(self.click_create, locatorType='css')
            time.sleep(2)
        self.Verification()

    add_sub_contact = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/p'''

    def LandlordCanHaveMultipleSubContacts(self):
        time.sleep(3)
        self.elementClick(self.landlord_tab)
        time.sleep(2)
        for i in range(1, 3):
            self.elementClick(self.add_sub_contact)
            self.RandomSubsidiary_company()
            time.sleep(2)
            self.elementClick(self.click_create, locatorType='css')
            time.sleep(4)
        self.Verification()

