import time
from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class DealList(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.ut = Util()
        self.driver = driver


    # Locators:

    # TC - 01 - Accessing Quick filters

    '''
    Steps:
    Login to app
    click on back arrow near need my approval text
    Click on My deals quick filter
    
    Expected:
    Only those deals that I am part of (as a team member) should be displayed.
    
    '''

    click_arrow_img = "//img[@class='sidebar--header-chevron']"
    click_my_deals = "//p[contains(text(),'My deals')]"
    active_tag = "//div[contains(text(),'Active')]"
    click_need_my_approval = "//p[contains(text(),'Needs my approval')]"
    click_pending_release = "//p[contains(text(),'Pending release')]"
    approve_release_button = "//span[contains(text(),'Approve release')]"

    def ClickNeedMyApproval(self):
        self.elementClick(self.click_need_my_approval)

    def ClickBackArrow(self):
        self.elementClick(self.click_arrow_img)

    def AccessMyDealQuickFilter(self):
        time.sleep(2)
        self.elementClick(self.click_arrow_img)
        time.sleep(2)
        self.elementClick(self.click_my_deals)
        time.sleep(2)
        active_text = self.getText(self.active_tag)
        tag_text = 'active'
        self.verifyTextContains(actualText=active_text, expectedText=tag_text)

    # test_02AccessNeedMyApproval

    def AccessNeedMyApprovalFilter(self):
        time.sleep(2)
        self.elementClick(self.click_arrow_img)
        time.sleep(2)
        self.ClickNeedMyApproval()
        time.sleep(3)
        button_text = self.getText(self.approve_release_button)
        button_original_text = "Approve release"
        self.verifyTextContains(actualText=button_text, expectedText=button_original_text)

    # test_03AccessPendingRelease

    tag1 = "//div[contains(text(),'Awaiting global approval')]"
    tag2 = "//div[contains(text(),'Awaiting regional approval')]"
    tag3 = "//div[contains(text(),'Awaiting release')]"
    tag4 = "//div[contains(text(),'Documents Required')]"

    def AccessPendingReleaseFilter(self):
        time.sleep(2)
        self.elementClick(self.click_arrow_img)
        time.sleep(2)
        self.elementClick(self.click_pending_release)
        time.sleep(2)
        tag1_text = self.getText(self.tag1)
        tag2_text = self.getText(self.tag2)
        tag3_text = self.getText(self.tag3)
        tag4_text = self.getText(self.tag4)
        self.verifyTextContains(actualText=tag1_text, expectedText='Awaiting global approval')
        self.log.info('tag1 verification passed')
        self.verifyTextContains(actualText=tag2_text, expectedText='Awaiting regional approval')
        self.log.info('tag2 verification passed')
        self.verifyTextContains(actualText=tag3_text, expectedText='Awaiting release')
        self.log.info('tag3 verification passed')
        self.verifyTextContains(actualText=tag4_text, expectedText='Documents Required')
        self.log.info('tag4 verification passed')


    # TC -C27808  Search box functionality

    '''
    Steps:
    1.Click on Search field
    2.Type some keywords (min. 2 keywords)
    3.Hit Enter
    
    Expected:
    Relevant search results should get displayed accordingly.
    
    '''

    first_deal_text = "//div[@class='deal-card---deal is-active']//div[@class='deal-card---top-row']"



    # TC - C27809 -- Adding New deal functionality

    '''
    Steps
    
    1.Click on + button from bottom left side of the screen
    2.Type any property address
    3.Click on any of the suggested properties
    4.Click on Add button
    
    Expected Result
    Deal should get created and should get displayed on the deal list screen

    '''

    # test_05AddingNewDealFunctionality

    click_add_new_deal = "//div[@class='add--new-deal']"
    new_deal_textbox = "//input[@id='search-bar-input']"
    click_add_button = "//div[@id='app']/div/div[2]/div/div/div/div/div[2]/div[2]/button"
    select_item_list = "//li[@id='search-bar-item-3']/div/p[2]"
    deal_name_main_page = "//div[@id='app']/div/div/div[2]/div/div[2]//div/h3"
    _toast_message = "//div[@class='Toastify__toast-body']"

    def EnterDeal(self, deal):
        self.sendKeys(deal, self.new_deal_textbox)


    def AddNewDeal(self, deal=''):
        time.sleep(2)
        self.elementClick(self.click_arrow_img)
        time.sleep(2)
        self.elementClick(self.click_add_new_deal)
        time.sleep(2)
        deal_name = self.ut.getUniqueName(3)
        self.EnterDeal(deal_name)
        time.sleep(3)
        self.elementClick(self.select_item_list)
        time.sleep(4)
        #deal_text = self.getElement(self.new_deal_textbox)
        #aa = deal_text.get_attribute('value')
        self.elementClick(self.click_add_button)
        time.sleep(5)
        success_message = self.getText(self._toast_message)
        success_msg = 'Deal successfully added'
        #deal_name_home = self.getText(self.deal_name_main_page)
        self.verifyTextContains(actualText=success_message, expectedText=success_msg)


    # TC -C27810 -- Adding New deal having deals already available

    '''
    
    Steps

    1.Click on + button from bottom left side of the screen
    2.Type any property address having deals already available
    3.Click on any of the suggested properties
    4.Click on Add button
    Expected Result
    
    New deal should get created and should get displayed on deal list screen
        
    '''

    # test_06AddingNewDealHavingDealsAlreadyAvailable

    deal_exist = "//div[@class='add-deal--has-existing']"
    cancel_button = "//button[contains(text(),'Cancel')]"


    def DealAlreadyAvailableText(self):
        time.sleep(2)
        self.elementClick(self.click_arrow_img)
        time.sleep(2)
        self.elementClick(self.click_add_new_deal)
        time.sleep(2)
        self.EnterDeal('Indi')
        time.sleep(3)
        self.elementClick(self.select_item_list)
        time.sleep(2)
        deal_exist_text = self.getText(self.deal_exist)
        deal_text = 'There are already 6 deals at this property. Add anyway?'
        self.verifyTextContains(actualText=deal_exist_text, expectedText=deal_text)
        self.elementClick(self.cancel_button)


    # TC - C27813 -- More filters with Region, Territory, Market, & Landlord fields

    '''
    
     Steps

    1.Click on More filters option
    2.Click on Region field
    3.Select any region from the list
    4.Click on Territory field
    5.Select any territory from the list
    6.Click on Market field
    7.Select any market from the list
    8.Click on Apply button
    Expected Result
    
    Deal list records should get changed according to the user's desirable filters
    
    '''

    # test_07RegionFieldFilter

    more_filter_icon = "//img[@src='/2/client/7ace26a7466f9ba855bb192b01aecb91.svg']"
    region_textfield = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div[1]'''
    external_click_close_dropdown = "//p[contains(text(),'Territory')]"
    select_region_list = "//p[contains(text(),'US & Canada East & Israel')]"
    check_after_filter_tag = "//div[contains(text(),'US & Canada East & Israel')]"

    def MoreFilterIcon(self):
        self.elementClick(self.more_filter_icon)

    # Verify Region Filter
    def RegionFilter(self):
        time.sleep(10)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.region_textfield)
        time.sleep(2)
        self.elementClick(self.select_region_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(3)
        tag_text = self.getText(self.check_after_filter_tag)
        tag_tax_verification = 'US & Canada East & Israel'
        self.verifyTextContains(actualText=tag_text, expectedText=tag_tax_verification)

    # test_08TerritoryFieldFilter

    territory_list = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div[1]'''
    select_territory_list = "//p[contains(text(),'South-Central')]"
    apply_button = "//button[contains(text(),'Apply')]"
    check_territory_tag = "//div[contains(text(),'South-Central')]"

    def ClickApplyButton(self):
        self.elementClick(self.apply_button)

    # Verify Territory Filter

    def TerritoryFilter(self):
        time.sleep(5)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.territory_list)
        time.sleep(2)
        self.elementClick(self.select_territory_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(3)
        territory_tag = self.getText(self.check_territory_tag)
        territory_tag_original = 'South-Central'
        self.verifyTextContains(actualText=territory_tag, expectedText=territory_tag_original)

    # test_09MarketFieldFilter

    market_list = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[3]/div/div/div[1]'''
    select_market_list = "//p[contains(text(),'Accra')]"
    check_market_Tag = "//div[contains(text(),'Accra')]"

    # Verify Market Filter

    def MarketFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.market_list)
        time.sleep(3)
        self.elementClick(self.select_market_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(3)
        market_tag = self.getText(self.check_market_Tag)
        market_tag_original = 'Accra'
        self.verifyTextContains(actualText=market_tag, expectedText=market_tag_original)



    # TC - C27814 More filters with Status, Stage, Team member, Release & Product type

    ''''
    Steps
    
    1.Click on More filters option
    2.Click on Status field
    3.Select any status from the list
    4.Click on Stage field
    5.Select any stage from the list
    6.Click on Release field
    7.Select any of the types from the list
    8.Click on Product type field
    9.Select any of the type from the list
    10.Click on Team member field
    11.Select any of the member from the list
    12.Click on Apply button
    Expected Result
    
    Deal list records should get changed according to the user's desirable filters
    
    '''
    # test_10StatusFieldFilter
    # Locators :

    status_field = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div/div[1]'''
    select_status_list = "//p[contains(text(),'Active')]"
    status_after_tag = "//div[contains(text(),'Active')]"

    # Verify status filter

    def StatusFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.status_field)
        time.sleep(2)
        self.elementClick(self.select_status_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(3)
        status_tag = self.getText(self.status_after_tag)
        status_tag_original = 'Active'
        self.verifyTextContains(actualText=status_tag, expectedText=status_tag_original)

    # test_11StageFieldFilter
    # Locators :

    stage_field = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div/div/div[1]'''
    select_stage_list = "//div[5]/div/div/div[2]/div/div/div/p[contains(text(),'Discovery')]"
    stage_after_tag = "//div[contains(text(),'E (Discovery)')]"


    def ClickStageField(self):
        self.elementClick(self.stage_field)

    # Verify stage filter

    def StageFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.stage_field)
        time.sleep(2)
        self.elementClick(self.select_stage_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        status_tag = self.getText(self.stage_after_tag)
        status_tag_original = 'E (Discovery)'
        self.verifyTextContains(actualText=status_tag, expectedText=status_tag_original)

    # test_12ReleaseFieldFilter
    # Locators :

    release_field = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[7]/div/div/div[1]'''
    select_release_list = "//p[contains(text(),'Awaiting regional approval')]"
    release_after_tag = "//div[contains(text(),'Awaiting regional approval')]"

    def ReleaseFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.release_field)
        time.sleep(2)
        self.elementClick(self.select_release_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        awaiting_tag = self.getText(self.release_after_tag)
        awaiting_tag_original = 'Awaiting regional approval'
        self.verifyTextContains(actualText=awaiting_tag, expectedText=awaiting_tag_original)

    # test_13ProductTypeFieldFilter
    # Verify Product Type Filter
    # Locators :

    product_type_field = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[8]/div/div/div[1]'''
    select_product_type_list = "//p[contains(text(),'Club')]"
    product_type_after_tag = "//div[contains(text(),'Club')]"

    def ProductTypeFilter(self):
        time.sleep(2)
        #scr1 = self.getElement(self.product_type_field)
        #self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.product_type_field)
        time.sleep(2)
        self.elementClick(self.select_product_type_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        awaiting_tag = self.getText(self.product_type_after_tag)
        awaiting_tag_original = 'Club'
        self.verifyTextContains(actualText=awaiting_tag, expectedText=awaiting_tag_original)


    team_member_field = '''//*[@id="app"]/div/div[2]/div/div/div[1]/div/div[2]/div[11]/div/div/div[1]'''
    select_team_member_list = "//p[contains(text(),'Shazadi Mohammed')]"
    team_member_after_tag = "//div[contains(text(),'Shazadi Mohammed')]"

    def EnterTeamName(self, name='sagar'):
        self.elementClick(self.team_member_field)
        time.sleep(2)
        self.sendKeys(name, self.team_member_field)

    def TeamMemberFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)

        ##### scroll into view #####
        element = self.getElement(self.scroll_possession)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")
        ##### scroll into view #####

        name = 'Shazadi Mohammed'
        self.EnterTeamName(name)
        time.sleep(2)
        self.elementClick(self.select_team_member_list)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        team_member_tag = self.getText(self.team_member_after_tag)
        self.verifyTextContains(actualText=team_member_tag, expectedText=name)


    #
    desk_input = "//div[12]//input[1]"
    desk_input2 = "//div[12]//input[2]"
    desk_after_tag = "//div[contains(text(),'desks: 100-1000')]"

    def DeskEnterNumber(self, num1=100, num2=1000):
        self.elementClick(self.desk_input)
        time.sleep(2)
        self.sendKeys(num1, self.desk_input)
        time.sleep(2)
        self.elementClick(self.desk_input2)
        time.sleep(2)
        self.sendKeys(num2, self.desk_input2)

    def DeskFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(3)
        # Enter desk number using desk method writtern above. Added default desk value.
        self.DeskEnterNumber()
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        desk_tag = self.getText(self.desk_after_tag)
        desk_original = 'desks: 100-1000'
        self.verifyTextContains(actualText=desk_tag, expectedText=desk_original)

    #
    rsf_input = "//div[13]//input[1]"
    rsf_input2 = "//div[13]//input[2]"
    rsf_after_tag = "//div[contains(text(),'rsf: 100-1000')]"

    def RsfEnterNumber(self, num1=100, num2=1000):
        self.elementClick(self.rsf_input)
        time.sleep(2)
        self.sendKeys(num1, self.rsf_input)
        time.sleep(2)
        self.elementClick(self.rsf_input2)
        time.sleep(2)
        self.sendKeys(num2, self.rsf_input2)

    def RSFFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(3)
        self.RsfEnterNumber()
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        desk_tag = self.getText(self.rsf_after_tag)
        desk_original = 'rsf: 100-1000'
        self.verifyTextContains(actualText=desk_tag, expectedText=desk_original)

    #
    usf_input = "//div[14]//input[1]"
    usf_input2 = "//div[14]//input[2]"
    usf_after_tag = "//div[contains(text(),'usf: 100-1000')]"

    def UsfEnterNumber(self, num1=100, num2=1000):
        self.elementClick(self.usf_input)
        time.sleep(2)
        self.sendKeys(num1, self.usf_input)
        time.sleep(2)
        self.elementClick(self.usf_input2)
        time.sleep(2)
        self.sendKeys(num2, self.usf_input2)

    def USFFilter(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(3)
        self.UsfEnterNumber()
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)
        desk_tag = self.getText(self.usf_after_tag)
        desk_original = 'usf: 100-1000'
        self.verifyTextContains(actualText=desk_tag, expectedText=desk_original)

    # css = .CalendarDay__today
    # id=possessionDate
    # xpath=(//input[@id='possessionDate'])[2]
    # id=(//input[@id='openingDate'])[1]
    # xpath=(//input[@id='openingDate'])[2]


    possession_date = "(//input[@id='possessionDate'])[1]"
    possession_end_date = "(//input[@id='possessionDate'])[2]"
    scroll_possession = "//p[contains(text(),'Possession date')]"
    select_date = ".CalendarDay__today"
    select_end_date = ".CalendarDay__hovered_span"
    possession_date_after_tag = "//div[contains(text(),'possession: ')]"

    def SelectFirstDateFromCalendar(self):
        self.elementClick(self.select_date, locatorType='CSS')

    def SelectLastDateWeekFromCalendar(self):
        self.elementClick(self.select_end_date, locatorType='CSS')

    def PosseDate(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)

        ##### scroll into view #####
        element = self.getElement(self.scroll_possession)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -350);")
        ##### scroll into view #####

        time.sleep(2)
        self.elementClick(self.possession_date)
        time.sleep(2)
        self.SelectFirstDateFromCalendar()
        time.sleep(2)
        self.SelectLastDateWeekFromCalendar()
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)

        ## Split the possession tag
        get_date_text = self.getText(self.possession_date_after_tag)
        get_date_text = get_date_text.split()
        get_date_text = get_date_text[0]
        # Verify result after split
        self.verifyTextContains(actualText=get_date_text, expectedText="possession:")


    opening_date = "(//input[@id='openingDate'])[1]"
    opening_end_date = "(//input[@id='openingDate'])[2]"
    opening_after_tag = "//div[contains(text(),'opening:')]"

    def OpeningDate(self):
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)

        ##### scroll into view #####
        element = self.getElement(self.scroll_possession)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")
        ##### scroll into view #####

        time.sleep(2)
        self.elementClick(self.opening_date)
        time.sleep(2)
        self.SelectFirstDateFromCalendar()
        time.sleep(2)
        self.SelectLastDateWeekFromCalendar()
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(2)

        ## Split the possession tag
        get_date_text = self.getText(self.opening_after_tag)
        get_date_text = get_date_text.split()
        get_date_text = get_date_text[0]
        # Verify result after split
        self.verifyTextContains(actualText=get_date_text, expectedText="opening:")



    # C27817 Pagination of deallist screen

    '''
          
    User should be logged into the app
    Steps
    
    1.Click on Next button from bottom-left panel of the screen
    2.Click on Previous button from bottom-left panel of the screen
    Expected Result
    
    User should get navigated to Next page & Previous page

    '''

    # pagination

    next_button = "//button[contains(text(),'Next')]"
    previous_button = "//button[contains(text(),'Previous')]"
    reset_button = "//button[contains(text(),'Reset')]"

    def Pagination(self):
        time.sleep(2)
        #self.elementClick(self.click_arrow_img)
        time.sleep(2)
        self.elementClick(self.more_filter_icon)
        time.sleep(2)
        self.elementClick(self.reset_button)
        time.sleep(2)
        self.elementClick(self.apply_button)
        time.sleep(4)
        ##### scroll into view #####
        element = self.getElement(self.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")
        ##### scroll into view #####
        time.sleep(2)
        self.elementClick(self.next_button)
        time.sleep(2)
        ##### scroll into view #####
        element = self.getElement(self.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")
        ##### scroll into view #####
        self.elementClick(self.previous_button)





























































