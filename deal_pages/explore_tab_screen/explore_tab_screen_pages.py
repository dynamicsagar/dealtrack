import time
from base.selenium_driver import SeleniumDriver
from utilities.util import Util
from selenium.webdriver import ActionChains


class ExploreScreen(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators:

    # C27818 - Explore screen

    '''
    
    User should be logged into the app
    Steps
    
    1.Click on Explore tab from left navigation panel
    Expected Result
    
    User should redirected to Explore screen
 
    '''

    explore_icon = "//a[3]//img[1]"
    explore_text = "//h3[contains(text(),'Explore')]"

    def ExploreNavigation(self):
        time.sleep(2)
        self.elementClick(self.explore_icon)
        time.sleep(2)
        text = 'Explore'
        actual_text = self.getText(self.explore_text)
        self.verifyTextContains(actualText=actual_text, expectedText=text)



    # C27819 Search functionality on Explore

    '''
    
    Preconditions
    
    User should be on Explore tab
    Steps
    
    1.Click on Search field
    2.Type some keywords (min. 3 keywords)
    Expected Result
    
    Search suggestions should get displayed accordingly
    
    '''

    search_textbox = "//input[@id='search-bar-input']"
    select_deal = "//li[@id='search-bar-item-3']/div/p[2]"

    def EnterDeal(self, name=''):
        self.elementClick(self.search_textbox)
        self.sendKeys(name, self.search_textbox)

    def SearchDeal(self):
        time.sleep(2)
        self.ut = Util()
        time.sleep(2)
        deal_name = self.ut.getUniqueName(4)
        self.EnterDeal(deal_name)
        time.sleep(3)
        self.elementClick(self.select_deal)
        time.sleep(10)


    # C27821 Adding a new deal from Explore tab

    '''
    
    Preconditions
    
    User should be on Explore tab
    Steps
    
    1.Click on Search field
    2.Type some keywords (min. 3 keywords)
    3.Click on any of suggested properties
    4.Click on Add a deal button, or
    5.Click on that property address
    6.Click on Add a deal button from details screen(empty screen)
    Expected Result
    
    Deal with that property address should get created and user should be redirected to deal details screen
    - Deal's(property) address should get displayed in the search box

    
    '''

    close_icon = "//*[@class='icon--close']"
    add_a_deal_button = "//button[contains(text(),'Add a deal')]"
    deal_detail_text_after_creation = "//button[contains(text(),'Release to D')]"


    def AddNewDeal(self):
        time.sleep(2)
        self.elementClick(self.close_icon)
        self.SearchDeal()
        self.elementClick(self.add_a_deal_button)
        time.sleep(3)
        text_deal_detail_page = self.getText(self.deal_detail_text_after_creation)
        text_detail = "Release to D (Sourcing)"
        self.verifyTextContains(actualText=text_deal_detail_page, expectedText=text_detail)


    # C27824 Zoom functionality on map-view

    '''
    
     Preconditions

    User should be on Explore tab
    Steps
    
    1.Zoom in/out on map view screen by clicking on +/- or scrolling up/down
    Expected Result
    
    Map view screen should display deals(pins) accordingly
     
    
    '''

    zoomin_button = "(//button[@type='button'])[3]"
    zoomout_button = "(//button[@type='button'])[4]"
    redo_Text = "//button[contains(text(),'Redo ')]"

    def ZoomFunctionality(self):
        time.sleep(2)
        self.elementClick(self.explore_icon)
        time.sleep(2)
        for i in range(4):
            self.elementClick(self.zoomin_button)
            time.sleep(2)
        for i in range(6):
            self.elementClick(self.zoomout_button)
            time.sleep(2)
        time.sleep(2)
        map_text = self.getText(self.redo_Text)
        original_text = "Redo search in this area"
        self.verifyTextContains(actualText=map_text, expectedText=original_text)


    # C27825 Street view on map screen

    '''
    
    Preconditions

    User should be on Explore tab
    Steps

    1.Drag-n-drop the street icon on map screen
    Expected Result

    Street view should get displayed on map screen
 
    
    '''

    street_icon = "//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div/div/div[8]/div[2]"
    drag_drop = "(//button[@type='button'])[2]"
    text_after_drop = "//a[contains(text(),'View on Google Maps')]"


    def StreetView(self):
        time.sleep(2)
        fromElement = self.getElement(self.street_icon)
        toElement = self.getElement(self.redo_Text)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(fromElement, toElement).perform()
        time.sleep(5)
        actions.click_and_hold(fromElement).move_to_element(toElement).release().perform()
        self.log.info("Drag And Drop Element Successful")
        time.sleep(4)
        street_text = self.getText(self.text_after_drop)
        street_text_verify = "View on Google Maps"
        self.verifyTextContains(actualText=street_text, expectedText=street_text_verify)



