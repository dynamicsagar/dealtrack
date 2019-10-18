import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.release.releasing_page import ReleasePage
from utilities.util import Util


class BrokerPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.release = ReleasePage(self.driver)
        self.ut = Util()
        self.driver = driver


    # C54671 Deal details > Broker


    '''
    
    Preconditions

    User should be logged into the app
    
    Step 	
    
    "Clicking broker section opens broker modal"

    1.User should scroll down to the broker section
    2.User should click on the section

    Expected:
    Broker modal should open
    
    '''

    broker = "//h4[contains(text(),'Broker')]"
    verify_edit_broker_modalbox = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/h2"

    def ClickingBrokerSectionOpensBrokerModal(self):
        time.sleep(2)
        self.deal.AddNewDeal()
        time.sleep(2)
        self.innerScroll(self.dealdetail.scroll_to_team)
        time.sleep(2)
        self.elementClick(self.broker)
        time.sleep(2)
        text = "Edit broker"
        broker_text = self.getText(self.verify_edit_broker_modalbox)
        self.verifyTextContains(actualText=broker_text, expectedText=text)


    # Deal details page has empty broker section
    '''
    
    "Deal details page has empty broker section"
    Precondition :
    - User should be logged into the app
    - User should be on deal details screen
    - There should be no broker yet
    
    1.User should scroll down to the broker section

    Expected Result
    It should say "Add Broker"
    
    '''

    add_broker_link = "//p[contains(.,'+ Add broker')]"

    def DealDetailsPageHasEmptyBrokerSection(self):
        time.sleep(2)
        text = "+ Add broker"
        text_link = self.getText(self.add_broker_link)
        self.verifyTextContains(actualText=text, expectedText=text_link)


    '''
    
    "Deal details page has "not applicable" broker section "
    Preconditions
    - User should be logged into the app
    - User should be on deal details screen
    - Broker should be not applicable (Find/Create a deal with Broker as "not applicable")
    
    1.Scroll down to broker section
    
    Expected : 
    There should be text in the broker section that says "Not applicable"
    
    '''

    not_applicable_link = "//p[contains(.,'Not applicable')]"

    def DealDetailsPageHasNotApplicableBrokerSection(self):
        time.sleep(2)
        text = "Not applicable"
        text_link = self.getText(self.not_applicable_link)
        self.verifyTextContains(actualText=text, expectedText=text_link)


    # Submit button should be disabled

    '''
    
    "Save is disabled until a broker or "not applicable" is selected"
    1.Scroll down to broker section
    2.Click on section, to open modal
    
    Expected :
    Submit button should be disabled

    '''

    save_button = "//button[contains(text(),'Save')]"

    def SubmitButtonShouldBeDisabled(self):
        time.sleep(2)
        element = self.getElement(self.save_button)
        result = element.is_enabled()
        self.log.info(result)
        return result



    #  "User can search or create a broker"

    '''
    
     "User can search or create a broker"

    1.Scroll down to broker section
    2.Click on section, to open modal
    3.In modal, select "Add broker"

    Expected : 
    User sees search
    typing into search triggers a dropdown list of brokers and an "add broker" option
    
    '''

    broker_textbox = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div/div/input"
    after_adding_broker = ".broker--name"
    select_broker = "//p[contains(.,'Gaurav Dave')]"

    def EnterBroker(self, brokername):
        self.elementClick(self.broker_textbox)
        time.sleep(2)
        self.sendKeys(brokername, self.broker_textbox)

    def UserCanSearchAndCreateABroker(self):
        time.sleep(2)
        self.elementClick(self.add_broker_link)
        time.sleep(2)
        brokername = "Gaurav dave"
        self.EnterBroker(brokername)
        self.elementClick(self.select_broker)
        time.sleep(2)
        self.elementClick(self.save_button)
        time.sleep(2)
        verify_broker = self.getText(self.after_adding_broker, locatorType='css')
        self.verifyTextContains(actualText=verify_broker, expectedText=brokername)

    # "User can edit contact "

    '''
    
    "User can edit contact "
    1.Scroll down to broker section
    2.Click on section, to open modal
    3.In modal, select "Add broker"
    4.Search and select an existing broker
        
    Expected :
    A card should appear under the existing brokers name with info filled in
    User should be able to edit that info
    
    '''

    edit_contact_text_box = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/input"
    select_edit_contact = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div"
    verify_edit_contact_on_detail_page = "//p[contains(.,'gdave@arcgate.com')]"

    '''
    
    Steps:
    1. Click broker
    2. Enter contact name
    3. Select from suggestion list
    4. Click save button
    
    Verify added info on deal detail screen
    
    '''


    def EditContactBox(self, contactname):
        self.elementClick(self.edit_contact_text_box)
        time.sleep(2)
        self.sendKeys(contactname, self.edit_contact_text_box)

    def UserCanEditContacts(self):
        time.sleep(2)
        self.elementClick(self.broker)
        time.sleep(2)
        contactname = "g"
        self.EditContactBox(contactname)
        time.sleep(2)
        self.elementClick(self.select_edit_contact)
        time.sleep(2)
        self.elementClick(self.save_button)
        time.sleep(3)
        email_contact = "gdave@arcgate.com"
        emailcontact = self.getText(self.verify_edit_contact_on_detail_page)
        self.verifyTextContains(actualText=email_contact, expectedText=emailcontact)


    # "User can create a new contact"

    '''
    
    "User can create a new contact"
    1.Scroll down to broker section
    2.Click on section, to open modal
    3.In modal, select "Add broker"
    4.Search and select an existing broker
    5.Click on "Add Contact"
    6.Enter Contact name
    7.Enter contact email
    8.press save
    
    Expected :
    Broker is selected and contact is stored. Broker section shows 
    Broker company name with contact card with name and email of broker contact
    
    '''

    click_create_new_broker = ".contact-search--create-option"
    contact_close_icon = ".contact--ex-icon"
    add_contact = ".contact--add"

    def ClickCreateNew(self):
        self.elementClick(self.click_create_new_broker, locatorType='css')

    def ClickAddContact(self):
        self.elementClick(self.add_contact, locatorType='css')

    def ClickContactCloseIcon(self):
        self.elementClick(self.contact_close_icon, locatorType='css')

    '''
    
    Steps:
    1. Click on broker 
    2. Click on close icon of added broker and remove it
    3. Click add broker link
    4. Enter broker name
    5. Click create 
    6. Enter contact name
    7. Click save button
    
    '''

    def UserCanCreateANewContact(self):
        time.sleep(2)
        self.elementClick(self.broker)
        time.sleep(2)
        self.ClickContactCloseIcon()
        time.sleep(2)
        self.elementClick(self.add_broker_link)
        time.sleep(2)
        name = "broker"
        brokername = self.ut.getUniqueName(2)
        brokername = name + brokername
        self.EnterBroker(brokername)
        time.sleep(2)
        self.ClickCreateNew()
        time.sleep(2)
        self.ClickAddContact()
        time.sleep(2)
        name = "broker"
        contactname = self.ut.getUniqueName(2)
        contactname = name + contactname
        self.EditContactBox(contactname)
        time.sleep(2)
        self.ClickCreateNew()
        time.sleep(2)
        self.elementClick(self.save_button)

























