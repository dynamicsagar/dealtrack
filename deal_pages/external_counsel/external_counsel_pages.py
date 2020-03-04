import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.release.releasing_page import ReleasePage
from deal_pages.broker.broker_pages import BrokerPages
from deal_pages.landlord.landlord_pages import LandlordPages
from utilities.util import Util


class ExternalCounselPages(SeleniumDriver):

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


    # Display External counsel

    '''
    Pre condition :
    
    
    User should be on deal details screen
    
    Note : Save button will be disabled until Firm has been added
    
    
    Steps:
    "External counsel appears below broker"

    1.Scroll to broker section
    2.Look below


    Expected: 
    User should see external counsel section

    
    '''

    contacts = "//a[contains(text(),'Contacts')]"
    text_external_counsel = "//h4[contains(text(),'External counsel')]"

    def ClickContacts(self):
        self.elementClick(self.contacts)

    def UserShouldSeeExternalCounselSection(self):
        self.deal.AddNewDeal()
        time.sleep(2)
        self.ClickContacts()
        time.sleep(2)
        self.elementPresenceCheck(self.text_external_counsel, byType='xpath')



    '''
    
    "External counsel has empty state"

    Add a new deal
    Go to new deal's deal details page
    Look at external counsel section

    Expected:
    Should say "Add external counsel"
    
    '''

    empty_label_text = "//p[contains(text(),'Add external counsel')]"

    def ExternalCounselHasEmptyState(self):
        time.sleep(2)
        self.elementPresenceCheck(self.empty_label_text, byType='xpath')



    '''
    
    "Clicking on external counsel section launches edit modal"

    1.Go to external counsel section
    2.Click section
    
    Expected:
    External counsel modal launches

    '''

    click_add_external_contact = ".contact--add"

    def ClickAddExternalContact(self):
        self.elementClick(self.click_add_external_contact, locatorType='css')

    def ClickingOnExternalCounselSectionLaunchesEditModal(self):
        time.sleep(2)
        self.elementClick(self.text_external_counsel)
        time.sleep(2)
        self.isElementDisplayed(self.click_add_external_contact, locatorType='css')


    '''
    
    "Clicking "+ add external counsel" shows typeahead"

    1.Scroll to external counsel section
    2.Launch external counsel modal
    3.Click on blue text that says "+ Add external counsel"

    
    Expected:
    Typeahead component should appear that has label "Firm name"


    '''

    firm_label = ".contact-search--input-label"


    def ClickingAddExternalCounselShowsTypeahead(self):
        time.sleep(2)
        self.ClickAddExternalContact()
        time.sleep(2)
        self.isElementDisplayed(self.firm_label, locatorType='css')


    # User can search for existing firms

    '''
    
    Preconditions

    User is logged into Dealtrack
    User is on deal details page of deal with no external counsel
    
    Steps

    1.Scroll to external counsel section
    2.Launch external counsel modal
    3.click on blue text that says "+ Add external counsel"
    4.Start typing in typeahead component
    
    Expected Result

    Dropdown should appear and results should populate if there are any
    bottom of dropdown should have blue text that says "+ Create "[text that user is typing in search]""

    
    '''

    add_new_firm_textbox = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div/div/input"
    click_existing_firm = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div"

    def AddNewFirm(self, frimname):
        time.sleep(2)
        self.elementClick(self.add_new_firm_textbox)
        time.sleep(2)
        self.sendKeys(frimname, self.add_new_firm_textbox)

    def UserCanSearchForExistingFirms(self):
        time.sleep(2)
        firmname = 'law'
        self.AddNewFirm(firmname)
        time.sleep(2)
        self.elementClick(self.click_existing_firm)


    # user can search for existing lawyer at firm or add new lawyer

    '''
    
    Preconditions

    User is logged into Dealtrack
    User is on deal details page of deal with no external counsel
    
    Steps:
    
    1.Scroll to external counsel section
    2.Launch external counsel modal
    3.click on blue text that says "+ Add external counsel"
    4.Type [some new value] into typeahead component
    5.Select existing firm
    6.In new card, click "add lawyer"
    
     Expected Result

    Typeahead should pre-populate with lawyers that exist at the firm already



    '''

    lawyer_textbox = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div/div/input"


    def EnterLawyer(self, landlord):
        self.elementClick(self.lawyer_textbox)
        time.sleep(2)
        self.sendKeys(landlord, self.lawyer_textbox)

    def RandomLawyerName(self):
        landname = 'landlord'
        name = self.ut.getUniqueName(4)
        name = landname + name
        self.EnterLawyer(name)

    verify_entered_lawyer = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/strong"

    def UserCanSearchForExistingLawyerAtFirmOrAddNewLawyer(self):
        time.sleep(2)
        self.ClickAddExternalContact()
        self.RandomLawyerName()
        time.sleep(2)
        self.broker.ClickCreateNew()
        time.sleep(2)
        self.elementPresenceCheck(self.verify_entered_lawyer, byType='xpath')

    # There can be multiple lawyers assigned to a deal

    '''
    
    Preconditions

    User is logged into Dealtrack
    User is on deal details page of deal with pre-existing external counsel firm and lawyers
    
     Steps

    1.Click on external counsel section to launch modal
    2.In modal, click "add lawyer" underneath current lawyers
    
     Expected Result

    User should be able to add as many lawyers as they want. They are displayed on the deal details page side by side in card view


    '''

    def ThereCanBeMultipleLawyersAssignedToADeal(self):
        time.sleep(2)
        for i in range(1, 4):
            self.ClickAddExternalContact()
            time.sleep(2)
            self.RandomLawyerName()
            time.sleep(2)
            self.broker.ClickCreateNew()
            time.sleep(2)
        self.elementClick(self.landlord.save_button)


    # Test 1. User is on deal details page of deal with external counsel that has firm and lawyers

    '''

    Preconditions

    User is logged into Dealtrack

       Test 1. User is on deal details page of deal with external counsel that has firm and lawyers

       Steps:
       Look at external counsel section

       Expected Result:

       Section should say "External counsel"
       Test 1 & 2: Firm should be displayed in bold text w/ icon

   '''

    lawyer_check = ".gvEbHU:nth-child(1)"

    def ExternalCounselThatHasFirmAndLawyers(self):
        time.sleep(2)
        self.elementPresenceCheck(self.counsel_icon, byType='xpath')
        self.isElementPresent(self.lawyer_check, locatorType='css')


    # Functionality behind removing Firm name and lawyers

    '''
    
     Preconditions

    User is logged into Dealtrack
    User is on deal details page of deal with pre-existing external counsel firm and one lawyer

    "User can remove lawyer by clicking 'x'"

    1.Launch external counsel modal
    2.On list of lawyers, click x next to lawyers name
    
    Expected:
    lawyer should be removed from the list
    their should be no lawyers left
    user should be able to save

    
    '''

    close_icon = "//div[@class='lawyer--search']//div[1]//img[2]"

    def UserCanRemoveLawyerByClickingX(self):
        time.sleep(2)
        self.elementClick(self.text_external_counsel)
        time.sleep(2)
        for i in range(1, 5):
            time.sleep(1)
            a = "//div[@class='lawyer--search']//div"
            x = [i]
            c = "//img[2]"
            icon = a + str(x) + c
            time.sleep(2)
            self.elementClick(icon)
        time.sleep(2)
        self.elementClick(self.landlord.save_button)


    # External counsel section shows firm.


    # Test 2. User is on deal details page of deal with external counsel that only has firm

    '''
    Steps:
    Look at external counsel section
    
    Expected:
    Test 2: lawyers should each have a card with full name
    
    '''

    counsel_icon = "//img[@class='counsel--icon']"

    def ExternalCounselShowsOnlyLawyers(self):
        time.sleep(2)
        self.elementPresenceCheck(self.counsel_icon, byType='xpath')


    # "When user clicks 'x' next to firm, it clears firm name and lawyers"

    '''
    
    "When user clicks 'x' next to firm, it clears firm name and lawyers"

    1.Launch external counsel modal
    2.Click x next to firm name
    
    Expected:
    user should see "+ add external counsel" button
    save button should be disabled

    
    '''

    firm_close_icon = ".firm--ex-icon"

    def WhenUserRemoveFirmUsingCrossIcon(self):
        time.sleep(2)
        self.elementClick(self.text_external_counsel)
        time.sleep(2)
        self.elementClick(self.firm_close_icon, locatorType='css')
        time.sleep(4)
        self.elementPresenceCheck(self.add_new_firm_textbox)



