import time
from base.selenium_driver import SeleniumDriver


class login(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''
    Add all the locators that will be used for login and logout screens.
    '''
    # Locators:

    _google_login_button = "//div[@class='auth0-lock-social-button-text']"
    _email_id_textfield = "//input[@id='identifierId']"
    _next_button = "//span[contains(text(),'Next')]"
    _password_textfield = "//input[@name='password']"
    _user_profile_icon = "//div[@class='dropdown--avatar']//img[@class='avatar sc-1jqauu8-0 gPdbSv']"
    _logout_link = "//p[contains(text(),'Sign out')]"
    login_verify = "//h3[contains(text(),'Needs my approval')]"



    def clickGoogleLoginButton(self):
        self.waitForElement(self._google_login_button)
        self.elementClick(self._google_login_button)

    def enterEmail(self, email):
        self.waitForElement(email, self._email_id_textfield)
        self.sendKeys(email, self._email_id_textfield)

    def clickNextButton(self):
        self.waitForElement(self._next_button)
        self.elementClick(self._next_button)

    def enterPassword(self, password):
        self.waitForElement(password,self._password_textfield)
        self.sendKeys(password,self._password_textfield)

    def clickUserProfileIcon(self):
        time.sleep(5)
        self.elementClick(self._user_profile_icon)

    def clickLogoutLink(self):
        time.sleep(5)
        self.elementClick(self._logout_link)

    # TC- 01 - Login to the app

    '''
    Steps:
    1.Open the web app
    2.Enter valid email address & password
    3.Click on "Login" button

    Result :
    User should be successfully Logged-in

    '''

    def ValidLoginForm(self, email="", password=""):
        self.clickGoogleLoginButton()
        time.sleep(2)
        self.enterEmail(email)
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.enterPassword(password)
        time.sleep(2)
        self.clickNextButton()


    def LoginVerification(self):
        self.waitForElement(self.login_verify)
        time.sleep(2)
        home_text = self.getText(self.login_verify)
        time.sleep(2)
        original_text = 'Needs my approval'
        self.verifyTextContains(actualText=home_text, expectedText=original_text)


    # TC -02 -- Logout of the app

    '''
     Steps

     1.Click on profile Account tab from bottom-left corner of the screen
     2.Click on Sign out button

     Expected 
     User should be successfully Logged out of the app

    '''

    def logout(self):
        time.sleep(2)
        self.clickUserProfileIcon()
        self.clickLogoutLink()

    def LogoutValidation(self):
        time.sleep(8)
        google_text = self.getText(self._google_login_button)
        google_original_text = 'Log in with Google'
        self.verifyTextContains(actualText=google_text, expectedText=google_original_text)

















