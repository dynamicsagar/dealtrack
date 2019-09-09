import time
from base.selenium_driver import SeleniumDriver
from deal_pages.login_and_logout.login_logout_page import login


class AccountPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.logs = login(self.driver)
        self.driver = driver


    # C27924 Account tab

    '''
    Preconditions

    User should be logged into the app
    Steps
    
    1.Click on Account tab from bottom-left navigation panel
    Expected Result
    
    Modal box should get opened up containing :
    - User's profile picture,& Name should be displayed on top
    - Edit profile
    - Chat with support
    - FAQs and How-To's
    - Signout
    all options should be displayed
    
    '''

    edit_profile_text = "//p[contains(text(),'Edit Profile')]"
    chat_with_support = "//p[contains(text(),'Chat with support')]"
    faq_and_how_to = '''//p[contains(text(),"FAQs and how-to's")]'''
    sign_out = "//p[contains(text(),'Sign out')]"


    def VerifyAccountTab(self):
        time.sleep(2)
        self.logs.clickUserProfileIcon()
        time.sleep(2)
        edit_profile = self.getText(self.edit_profile_text)
        chat_support = self.getText(self.chat_with_support)
        faqs = self.getText(self.faq_and_how_to)
        sign_out_link = self.getText(self.sign_out)
        editprofile = "Edit Profile"
        chatsupport = "Chat with support"
        faq = '''FAQs and how-to's'''
        signout = "Sign out"
        self.verifyTextContains(actualText=edit_profile, expectedText=editprofile)
        self.log.info(" !!!!! Edit profile verification successfully !!!!")
        self.verifyTextContains(actualText=chat_support, expectedText=chatsupport)
        self.log.info(" !!!!! Chat with support verification successfully !!!!")
        self.verifyTextContains(actualText=faqs, expectedText=faq)
        self.log.info(" !!!!! FAQs and how-to's verification successfully !!!!")
        self.verifyTextContains(actualText=sign_out_link, expectedText=signout)
        self.log.info(" !!!!! Sign out verification successfully !!!!")

    # C27925 Edit Profile

    '''
    Preconditions

    User should be logged into the app
    Steps
    
    1.Click on Account tab from bottom-left navigation panel
    2.Click on Edit profile option
    Expected Result
    
    Edit profile modal box should get displayed

    '''

    region_text = "//span[contains(text(),'Region')]"

    def EditProfile(self):
        time.sleep(2)
        self.elementClick(self.edit_profile_text)
        time.sleep(2)
        region = self.getText(self.region_text)
        verify_region = "Region"
        self.verifyTextContains(actualText=region, expectedText=verify_region)
        self.log.info(" !!!!! Sign out verification successfully !!!!")


    # C27926 Editing Region, Territory & Role

    '''
    Preconditions

    User should be on Edit profile modal box
    Steps
    
    1.Click on Region field
    2.Select any of the region from the list
    3.Click on Territory field
    4.Select any of the territory from the list
    5.Click on Role field
    6.Click on any of the role from the list
    7.Validate sort order in all three fields (Region, Territory & Roles)
    8.Click on Save button
    Expected Result
    
    User's region, territory, & role should get changed and its sort order is as expected
    
    Note : Role should be displayed in alphabetical order
 
    '''

    click_region_drop = "//select[@name='region']"
    select_region = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div/div[2]/select/option[5]"
    territory = "//select[@name='territory']"
    select_territory = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/select/option[2]"
    click_role = "//select[@name='role']"
    select_role = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/select/option[3]"
    save_button = "//button[contains(text(),'Save')]"

    def SelectRegion(self):
        time.sleep(2)
        self.elementClick(self.click_region_drop)
        time.sleep(2)
        self.elementClick(self.select_region)
        re = self.getText(self.click_region_drop)
        region_india = "US & Canada West"
        self.verifyTextContains(actualText=re, expectedText=region_india)
        self.log.info(" !!!!! SelectRegion verification successfully !!!!")
        time.sleep(2)
        self.elementClick(self.territory)
        time.sleep(2)
        self.elementClick(self.select_territory)
        time.sleep(2)
        territory_text = self.getText(self.territory)
        territory_value = "Northern California"
        self.verifyTextContains(actualText=territory_text, expectedText=territory_value)
        self.log.info(" !!!!! territory verification successfully !!!!")
        time.sleep(2)
        self.elementClick(self.click_role)
        time.sleep(2)
        self.elementClick(self.select_role)
        time.sleep(2)
        role_text = self.getText(self.click_role)
        role_value = "CweO"
        self.verifyTextContains(actualText=role_text, expectedText=role_value)
        self.log.info(" !!!!! role_value verification successfully !!!!")
        time.sleep(2)
        self.elementClick(self.save_button)


    # C27927 Chat with support & FAQ-Hows To

    '''
     Preconditions

    User should be on Edit profile modal box
    Steps
    
    1.Click on Chat with support
    2.Click on FAQ & How's To
    Expected Result
    
    User should redirected to relative screens
 
    '''

    start_conversation_text = "//h2[contains(.,'Start a conversation')]"

    def ChatSupport(self):
        time.sleep(2)
        self.logs.clickUserProfileIcon()
        time.sleep(2)
        self.elementClick(self.chat_with_support)
        time.sleep(2)
        text = self.getText(self.start_conversation_text)
        time.sleep(2)
        self.driver.switch_to_frame(0)
        original_text = "Start a conversation"
        self.verifyTextContains(actualText=text, expectedText=original_text)
        self.log.info(" !!!!! ChatSupport verification successfully !!!!")

    navigation_page_header = '''//p[contains(text(),"FAQs")]'''

    def Faq(self):
        time.sleep(2)
        self.logs.clickUserProfileIcon()
        time.sleep(2)
        window_before = self.driver.window_handles[0]
        self.elementClick(self.faq_and_how_to)
        window_after = self.driver.window_handles[1]

        # switch on to new child window
        self.driver.switch_to.window(window_after)
        result = self.isElementDisplayed(self.navigation_page_header)










