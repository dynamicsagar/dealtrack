import time
import datetime
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from selenium.webdriver.common.keys import Keys


class DealDetailScreenPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deall = DealList(self.driver)
        self.driver = driver


    # Locators:

    # C27833  Deal details

    '''
     Preconditions
    
    User should be logged into the app
    Steps
    
    1.Create a new deal
    2.Click on newly created deal
    Expected Result
    
    User should redirect to deal details screen

    '''

    def DealDetails(self):
        time.sleep(2)
        self.deall.AddNewDeal()


    # C27834 Deal details adding/editing pictures, description, dealteam members, comments

    '''
     Preconditions

    User should be on deal details screen
    Steps
    
    1.Click on New Photo button link on each tag section
    2.Add some photos
    3.Click on description field
    4.Enter some description related to deal
    5.Click on each (+)link tag section under Document field
    6.Add few attachments
    7.Click on deal team field
    8.Add 5 deal team members
    Expected Result
    
    Data should get reflected on deal details screen for all the fields mentioned

    '''

    click_new_photo = "//span[contains(text(),'New photo')]"
    click_upload_popup = "//input[@id='fsp-fileUpload']"
    click_upload_button = "//span[contains(text(),'Upload')]"
    click_uploaded_image = '.tag > img'
    check_after_photo_upload = "//span[contains(text(),'Photos')]"
    click_close_icon = "//img[@alt='Close']"


    # Created a function to upload the documents.


    def UploadDocuments(self, name):
        self.getElement(self.click_upload_popup)
        self.sendKeys(name, self.click_upload_popup)

    def AddPhotos(self, name=''):
        time.sleep(2)
        self.elementClick(self.click_new_photo)
        time.sleep(2)
        # self.driver.switch_to.frame(0)
        name = "C:/Users/Sagar/Desktop/360degreeimages/R0010005.JPG"
        self.UploadDocuments(name)
        time.sleep(4)
        self.elementClick(self.click_upload_button)
        time.sleep(40)
        upload_text = "Photos"
        self.elementClick(self.click_uploaded_image, locatorType='css')
        time.sleep(2)
        get_upload_text = self.getText(self.check_after_photo_upload)
        self.verifyTextContains(actualText=get_upload_text, expectedText=upload_text)
        time.sleep(2)
        self.elementClick(self.click_close_icon)

    click_description = "//h4[contains(.,'Description')]"
    enter_description = "//textarea[@name='description']"
    click_Save_button = "//button[contains(.,'Save')]"
    description_text = "//p[contains(text(),'Hi this is a random automation text')]"

    def EnterDesc(self, description):
        self.elementClick(self.enter_description)
        self.clearField(self.enter_description)
        self.sendKeys(description, self.enter_description)

    def Description(self):
        time.sleep(2)
        self.elementClick(self.click_description)
        time.sleep(2)
        text_desc = "Hi this is a random automation text"
        self.EnterDesc(text_desc)
        time.sleep(2)
        self.elementClick(self.click_Save_button)
        time.sleep(2)
        # self.elementClick(self.click_description)
        # time.sleep(2)
        # desc_value = self.getElement(self.enter_description).get_attribute('value')
        time.sleep(2)
        desc_value = self.getText(self.description_text)
        self.verifyTextContains(actualText=desc_value, expectedText=text_desc)
        time.sleep(2)
        self.elementClick(self.click_Save_button)


    # Steps for Financial, term sheet and demo
    '''
    
    1. Login to app
    2. After entering description scroll the screen to documents section
    3. Click on financial model 
    4. Upload the documents
    5. Now click on term and similarly deal memo
    6. Upload the documents.

    '''

    click_financial = "//div[8]/div[2]/div[1]/div[2]/div"
    click_deal_memo = "//div[8]/div[2]/div[3]/div[2]/div"
    click_term_sheet = "//div[8]/div[2]/div[2]/div[2]/div"
    scroll_to_text = "//span[contains(text(),'Financial model')]"
    text_after_upload_financial_pdf = "//span[contains(text(),'E (Discovery)')]"


    def FinacialDocuments(self):
        time.sleep(15)
        self.innerScroll(self.scroll_to_text)
        time.sleep(2)
        self.elementClick(self.click_financial)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/FiMo.xlsm"
        self.UploadDocuments(doc)
        time.sleep(45)
        # text = 'E (Discovery)'
        # text_after_upload = self.getText(self.text_after_upload_financial_pdf)
        # self.verifyTextContains(actualText=text_after_upload, expectedText=text)

    def TermSheetDocument(self):
        time.sleep(2)
        self.elementClick(self.click_term_sheet)
        time.sleep(2)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/1.pdf"
        self.UploadDocuments(doc)
        time.sleep(35)

    def DealMemo(self):
        time.sleep(2)
        self.elementClick(self.click_deal_memo)
        time.sleep(2)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/DealMemo.pdf"
        self.UploadDocuments(doc)
        time.sleep(35)


    # Steps for team section
    '''
    Test case:
    1. login to app
    2. Scroll to team section on deal detail screen
    3. Click on team 
    4. Enter value 
    5. Click save button
    6. Click on team
    7. Get value of last entered value
    
    Verify entered values matches with the field. 
    
    '''

    scroll_to_team = "//h4[contains(text(),'Team')]"
    enter_real_state_manager = "//div[@id='app']//div[2]/div[1]/div[1]/div/div[1]/input"
    select_real_state_manager_value = "//li[contains(.,'Rumi Begum')]"
    click_team_save_button = "//button[contains(text(),'Save')]"

    def SaveButton(self):
        self.elementClick(self.click_team_save_button)

    def EnterRealManager(self, name):
        self.elementClick(self.enter_real_state_manager)
        time.sleep(2)
        self.sendKeys(name, self.enter_real_state_manager)

    def SelectRealStateManagerValue(self):
        name = "Rumi Begum"
        self.EnterRealManager(name)
        time.sleep(2)
        self.elementClick(self.select_real_state_manager_value)

    def TeamMemberRealStateManager(self):
        time.sleep(2)
        self.innerScroll(self.scroll_to_team)
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        name = "Rumi Begum"
        self.SelectRealStateManagerValue()
        self.elementClick(self.click_team_save_button)
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        real_state = self.getElement(self.enter_real_state_manager).get_attribute('value')
        time.sleep(2)
        self.verifyTextContains(actualText=real_state,expectedText=name)

    enter_transaction_manager = "//div[2]/div/div/input"
    select_transaction_manager_value = "//li[contains(.,'Rumi Begum')]"

    def EnterTransactionManager(self, name):
        self.elementClick(self.enter_transaction_manager)
        time.sleep(2)
        self.sendKeys(name, self.enter_transaction_manager)

    def SelectTransactionManager(self):
        name = "Rumi Begum"
        self.EnterTransactionManager(name)
        time.sleep(3)
        self.elementClick(self.select_transaction_manager_value)
        time.sleep(2)

    def TransactionManger(self):
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        name = "Rumi Begum"
        self.SelectTransactionManager()
        self.elementClick(self.click_team_save_button)
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        transaction_manager = self.getElement(self.enter_transaction_manager).get_attribute('value')
        time.sleep(2)
        self.verifyTextContains(actualText=transaction_manager, expectedText=name)

    enter_sourcer = "//div[3]/div/div/input"
    select_sourcer_value = "//li[contains(.,'Gaurav Dave')]"

    def EnterSourcer(self, name):
        self.elementClick(self.enter_sourcer)
        time.sleep(2)
        self.sendKeys(name, self.enter_sourcer)

    def SelectSourcer(self):
        name = 'Gaurav Dave'
        self.EnterSourcer(name)
        time.sleep(3)
        self.elementClick(self.select_sourcer_value)
        time.sleep(2)

    def Sourcer(self):
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        name = 'Gaurav Dave'
        self.SelectSourcer()
        self.elementClick(self.click_team_save_button)
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        sourcer = self.getElement(self.enter_sourcer).get_attribute('value')
        time.sleep(2)
        self.verifyTextContains(actualText=sourcer, expectedText=name)

    enter_real_state_analyst = "//div[4]/div/div/input"
    select_real_state_analyst_value = "//li[contains(.,'Shazadi Mohammed')]"

    def EnterRealState(self, name):
        self.elementClick(self.enter_real_state_analyst)
        time.sleep(2)
        self.sendKeys(name, self.enter_real_state_analyst)

    def SelectRealStateAnalystValue(self):
        name = 'Shazadi Mohammed'
        self.EnterRealState(name)
        time.sleep(3)
        self.elementClick(self.select_real_state_analyst_value)
        time.sleep(2)

    def RealStateAnalyst(self):
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        name = 'Shazadi Mohammed'
        self.SelectRealStateAnalystValue()
        self.elementClick(self.click_team_save_button)
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        real_state = self.getElement(self.enter_real_state_analyst).get_attribute('value')
        time.sleep(2)
        self.verifyTextContains(actualText=real_state, expectedText=name)

    # Locators for internal counsels
    enter_internal_counsel = "//div[5]/div/div/input"
    select_internal_counsel_value = "//li[contains(.,'Shazadi Mohammed')]"

    # Method to enter value in the text field
    def EnterInternalCounsel(self, name):
        self.elementClick(self.enter_internal_counsel)
        time.sleep(2)
        self.sendKeys(name, self.enter_internal_counsel)

    # Entering and selecting the value from the suggestion list
    def SelectInternalCounsel(self):
        name = 'Shazadi Mohammed'
        self.EnterInternalCounsel(name)
        time.sleep(3)
        self.elementClick(self.select_internal_counsel_value)
        time.sleep(2)

    # Method to save the value and verify the selection matches and showing correctly on the team screen.
    def InternalCounsel(self):
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        name = 'Shazadi Mohammed'
        self.SelectInternalCounsel()
        self.elementClick(self.click_team_save_button)
        time.sleep(2)
        self.elementClick(self.scroll_to_team)
        time.sleep(2)
        internal_counsel = self.getElement(self.enter_internal_counsel).get_attribute('value')
        time.sleep(2)
        self.verifyTextContains(actualText=internal_counsel, expectedText=name)
        self.elementClick(self.click_team_save_button)


    # C27836 Deal details adding/editing data for Genaral Info, Terms, Performance & Floors tab

    '''
    Preconditions
    
    User should be on deal details screen
    Steps
    
    1.Click on General Info tab
    2.Add values in Market, product type (adding, removing multiple product types), Desks, USF, RSF, Possession, Opening & Tour completed fields
    3.Click on Save button
    4.Click on Terms tab
    5.Add values in Dealtype, Gross rent, Net rent, OpEx, TI allowance, Free rent, Lease term & Signage fields
    6.Click on Save button
    7.Click on Performance tab
    8.Add values in EBITDA margin, Breakeven occupancy, payback period, Net effective rent, Gross NPV, Adjusted NPV, Annual escalations, Loss factor, Effect on capEx, Effect on desk goals, Letter of creditY1, Corporate Guarantee fields
    9.Click on Save button
    10.Click on Floors tab
    11.Click on Add floors link
    12.Type floor number and hit Enter
    13.Add values in all subfields
    14.Click on Save button
    Expected Result
    
    Data should get reflected on deal details screen for all the fields mentioned

    '''

    scroll_to_general_tab = "//div[contains(text(),'General')]"
    click_to_open_general_tab = "//span[contains(text(),'Desks')]"
    enter_desk_value = "//input[@name='desks']"
    enter_usf_value = "//input[@name='usf']"
    enter_rsf_value = "//input[@name='rsf']"
    click_yes = "//label/p[contains(text(),'Yes')]"
    check_desk = "//li[4]//span[2]"
    check_usf = "//li[5]//span[2]"
    check_rsf = "//li[6]//span[2]"
    check_tour_completed = "//li[9]//span[2]"

    def CheckLabelYes(self):
        self.elementClick(self.click_yes)

    def EnterDeskValue(self, num):
        self.elementClick(self.enter_desk_value)
        time.sleep(1)
        self.sendKeys(num, self.enter_desk_value)

    def EnterUSFValue(self, usfnum):
        self.elementClick(self.enter_usf_value)
        time.sleep(1)
        self.sendKeys(usfnum, self.enter_usf_value)

    def EnterRSFValue(self, rsfnum):
        self.elementClick(self.enter_rsf_value)
        time.sleep(1)
        self.sendKeys(rsfnum, self.enter_rsf_value)

    def GeneralInfoTab(self):
        time.sleep(2)
        self.innerScrollUp(self.scroll_to_general_tab)
        time.sleep(2)
        self.elementClick(self.click_to_open_general_tab)
        time.sleep(2)
        num = '100'
        self.EnterDeskValue(num)
        time.sleep(2)
        usfnum = '100'
        self.EnterUSFValue(usfnum)
        time.sleep(2)
        rsfnum = '100'
        self.EnterRSFValue(rsfnum)
        time.sleep(2)
        self.innerScroll(self.click_yes)
        time.sleep(2)
        self.CheckLabelYes()
        time.sleep(2)
        self.elementClick(self.click_Save_button)
        time.sleep(2)
        desk_name = self.getText(self.check_desk)
        # desk_name = desk_name.split()
        # desk_name = desk_name[1]
        time.sleep(2)
        rsfname = self.getText(self.check_rsf)
        # rsfname = rsfname.split()
        # rsfname = rsfname[1]
        time.sleep(2)
        usfname = self.getText(self.check_usf)
        # usfname = usfname.split()
        # usfname = usfname[1]
        time.sleep(2)
        self.verifyTextContains(actualText=desk_name, expectedText=num)
        self.verifyTextContains(actualText=usfname, expectedText=usfnum)
        self.verifyTextContains(actualText=rsfname, expectedText=rsfnum)


    click_terms_tab = "//div[contains(text(),'Terms')]"
    click_to_open_terms_tab = "//span[contains(text(),'Gross')]"
    click_rental_type_dropdown = "//select[@name='rentType']"
    click_rfi_lease = "//option[@value='FRI']"
    enter_gross_rent = "//input[@name='grossRentPerMonthNotes']"
    enter_opEx = "//input[@name='opEx']"
    enter_allowance = "//input[@name='tiAllowanceNotes']"
    enter_free_rent = "//input[@name='freeRentMonthsNotes']"
    enter_lease_term = "//input[@name='termMonthsNotes']"
    check_gross_rent = "//li[3]//span[2]"
    check_rfi_lease = "//li[2]//span[2]"
    check_opEx = "//li[4]//span[2]"
    check_allowance = "//li[5]//span[2]"
    check_free_rent = "//li[6]//span[2]"
    check_lease_term = "//li[7]//span[2]"
    check_signange = "//li[8]//span[2]"

    def EnterGrossRent(self, gross_rent):
        self.elementClick(self.enter_gross_rent)
        time.sleep(1)
        self.sendKeys(gross_rent, self.enter_gross_rent)

    def EnterOpEx(self, op_ex):
        self.elementClick(self.enter_opEx)
        time.sleep(1)
        self.sendKeys(op_ex, self.enter_opEx)

    def EnterAllowances(self, allow):
        self.elementClick(self.enter_allowance)
        time.sleep(1)
        self.sendKeys(allow, self.enter_allowance)

    def EnterFreeRent(self, rent):
        self.elementClick(self.enter_free_rent)
        time.sleep(1)
        self.sendKeys(rent, self.enter_free_rent)

    def EnterLeaseTerm(self, lease):
        self.elementClick(self.enter_lease_term)
        time.sleep(1)
        self.sendKeys(lease, self.enter_lease_term)

    def TermsTab(self):
        time.sleep(2)
        self.elementClick(self.click_terms_tab)
        time.sleep(2)
        self.elementClick(self.click_to_open_terms_tab)
        time.sleep(2)
        self.elementClick(self.click_rental_type_dropdown)
        time.sleep(2)
        self.elementClick(self.click_rfi_lease)
        time.sleep(2)
        gross_rent = '300'
        self.EnterGrossRent(gross_rent)
        time.sleep(2)
        op_ex = "400"
        self.EnterOpEx(op_ex)
        time.sleep(2)
        allow = "400"
        self.EnterAllowances(allow)
        time.sleep(2)
        self.innerScroll(self.click_yes)
        time.sleep(2)
        rent = "500"
        self.EnterFreeRent(rent)
        time.sleep(2)
        lease = "600"
        self.EnterLeaseTerm(lease)
        time.sleep(2)
        self.CheckLabelYes()
        time.sleep(2)
        self.elementClick(self.click_Save_button)
        time.sleep(4)
        rfi_lease = self.getText(self.check_rfi_lease)
        rfilease = 'FRI – Lease'
        grossrent = self.getText(self.check_gross_rent)
        # grossrent = grossrent.split()
        # grossrent = grossrent[1]
        time.sleep(2)
        opEx = self.getText(self.check_opEx)
        # opEx = opEx.split()
        # opEx = opEx[1]
        time.sleep(2)
        allowances = self.getText(self.check_allowance)
        # allowances = allowances.split()
        # allowances = allowances[1]
        time.sleep(2)
        freerent = self.getText(self.check_free_rent)
        # freerent = freerent.split()
        # freerent = freerent[1]
        time.sleep(2)
        leaseterm = self.getText(self.check_lease_term)
        # leaseterm = leaseterm.split()
        # leaseterm = leaseterm[1]
        time.sleep(2)
        signage = 'Yes'
        signa = self.getText(self.check_signange)
        # signa = signa.split()
        # signa = signa[1]
        self.verifyTextContains(actualText=rfi_lease, expectedText=rfilease)
        # self.verifyTextContains(actualText=grossrent, expectedText=gross_rent)
        # self.log.info('!!!! Gross rent verification successfully !!!!')
        # self.verifyTextContains(actualText=opEx, expectedText=op_ex)
        # self.log.info('!!! OPEX verification successfully !!!!')
        # self.verifyTextContains(actualText=allowances, expectedText=allow)
        # self.log.info('!!! allowances verification successfully !!!!')
        # self.verifyTextContains(actualText=freerent, expectedText=rent)
        # self.log.info('!!!! Free rent verification successfully !!!!')
        # self.verifyTextContains(actualText=leaseterm, expectedText=lease)
        # self.log.info('!!!! Lease Term verification successfully !!!!')
        self.verifyTextContains(actualText=signa, expectedText=signage)
        # self.log.info('!!!! signage verification successfully !!!!')


    click_performance_tab = "//div[contains(text(),'Performance')]"
    click_to_open_performance_tab = "//span[contains(text(),'Payback period')]"
    enter_ebitda_margin = "=//input[@name='ebitdaMargin']"
    enter_breakeven_occupancy = "//input[@name='breakevenOccupancy']"
    enter_payback_period = "//input[@name='paybackPeriod']"
    enter_net_effective_rent = "//input[@name='netEffectiveRent']"
    enter_gross_npv = "//input[@name='grossNpv']"
    enter_adjusted_npv = "//input[@name='adjustedNpv']"
    enter_gross_construction_cost = "//input[@name='grossConstructionCost']"


    def EnterEbditaMargin(self, ebdita):
        self.elementClick(self.enter_ebitda_margin)
        time.sleep(2)
        self.sendKeys(ebdita, self.enter_ebitda_margin)

    def EnterBreakEven(self, breakeven):
        self.elementClick(self.enter_breakeven_occupancy)
        time.sleep(2)
        self.sendKeys(breakeven, self.enter_breakeven_occupancy)

    def EnterPayBackPeriod(self, payback):
        self.elementClick(self.enter_payback_period)
        time.sleep(2)
        self.sendKeys(payback, self.enter_payback_period)

    def EnterNetEffectiveRent(self, neteffective):
        self.elementClick(self.enter_net_effective_rent)
        time.sleep(2)
        self.sendKeys(neteffective, self.enter_net_effective_rent)

    def EnterGrossNPV(self, grossnpv):
        self.elementClick(self.enter_gross_npv)
        time.sleep(2)
        self.sendKeys(grossnpv, self.enter_gross_npv)

    def EnterAdjustedNPV(self, adjustednpv):
        self.elementClick(self.enter_adjusted_npv)
        time.sleep(2)
        self.sendKeys(adjustednpv, self.enter_adjusted_npv)

    def EnterGrossConstructionCost(self, grossconstructioncost):
        self.elementClick(self.enter_gross_construction_cost)
        self.clearField(self.enter_gross_construction_cost)
        time.sleep(2)
        self.sendKeys(grossconstructioncost, self.enter_gross_construction_cost)

    def PerformanceTab(self):
        time.sleep(2)
        self.elementClick(self.click_performance_tab)
        time.sleep(2)
        self.elementClick(self.click_to_open_performance_tab)
        time.sleep(2)
        ebdita = '30.3'
        self.EnterEbditaMargin(ebdita)
        time.sleep(2)
        breakeven = "40"
        self.EnterBreakEven(breakeven)
        time.sleep(2)
        payback = "37.95"
        self.EnterPayBackPeriod(payback)
        time.sleep(2)
        neteffective = '25'
        self.EnterNetEffectiveRent(neteffective)
        time.sleep(2)
        grossnpv = "21015"
        self.EnterGrossNPV(grossnpv)
        time.sleep(2)
        adjustednpv = "25425"
        self.EnterAdjustedNPV(adjustednpv)
        time.sleep(2)
        grossconstructioncost1 = "2580985"
        self.EnterGrossConstructionCost(grossconstructioncost1)
        time.sleep(2)
        self.elementClick(self.click_Save_button)
        time.sleep(4)
        g_value1 = self.getText(self.check_gross_value)
        g_value1 = g_value1.replace("$", '')
        g_value1 = g_value1.replace(",", '')
        self.verifyTextContains(actualText=g_value1, expectedText=grossconstructioncost1)

    click_floors_tab = "//div[contains(text(),'Floors')]"
    click_to_open_floors_tab = "//p[contains(text(),'Add floors')]"
    enter_floor = "//div[@id='app']/div/div[2]/div/div/div/div[2]/div/input"
    enter_rsf = "//td[2]//input[1]"
    enter_usf = "//td[3]//input[1]"
    enter_desk = "//td[4]//input[1]"
    check_rsf_after = "//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div[7]/div/div[2]/div/div/ol/li/span[2]"
    enter_possession_date = "//td[5]//div[1]//div[1]//div[1]//div[1]//div[1]//input[1]"
    enter_opening_date = "//td[6]//div[1]//div[1]//div[1]//div[1]//div[1]//input[1]"


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

    def FloorsTab(self):
        time.sleep(2)
        self.elementClick(self.click_floors_tab)
        time.sleep(2)
        self.elementClick(self.click_to_open_floors_tab)
        time.sleep(2)
        self.EnteringFloorValues()
        time.sleep(2)
        rsf_num = '10'
        rsf = self.getText(self.check_rsf_after)
        self.verifyTextContains(actualText=rsf, expectedText=rsf_num)

    def EnteringFloorValues(self):
        floor_num = '2'
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
        self.DateSelectionPossessionAndOpeningDate()
        time.sleep(2)
        self.elementClick(self.click_Save_button)

    # Below methods we have created to enter opening and closing date

    def EnterFloorPossessionDate(self, pos_date):
        self.elementClick(self.enter_possession_date)
        time.sleep(2)
        self.sendKeys(pos_date, self.enter_possession_date)

    def EnterFloorOpeningDate(self, opening_date):
        self.elementClick(self.enter_opening_date)
        time.sleep(2)
        self.sendKeys(opening_date, self.enter_opening_date)

    '''
    Steps:
    1. use today's date using date time inbuilt function
    2. for loop and select next date
    3. next date used for possession 
    4. in else condition :
    5. use day after tomorrow date i.e opening date
    
    '''

    def DateSelectionPossessionAndOpeningDate(self):
        base = datetime.datetime.now()
        for x in range(1, 3):
            if x == 1:
                a = (base + datetime.timedelta(days=x))
                a = (a.strftime("%m/%d/%Y"))
                self.log.info(a)
                self.EnterFloorPossessionDate(a)
            else:
                a = (base + datetime.timedelta(days=x))
                a = (a.strftime("%m/%d/%Y"))
                self.log.info(a)
                time.sleep(2)
                self.EnterFloorOpeningDate(a)



    # C27837 Timeline > Milestones, Approval activity, Comments

    '''
     Preconditions
    
    User should be logged into the app
    Steps
    
    1.Create a new deal
    2.Click on newly created deal
    3.Click on comments section
    4.Add some comment & click on Send button
    5.Release the deal to stage D
    6.Release the deal to stage C
    7.Requests the deal
    8.Request changes the deal
    9.Cancel the release
    10.Approve the deal
    Expected Result
    
    Everything related to deal creation, approval requests, approvals, comments should get displayed under Timeline section
    
    '''

    comment_box = "//textarea[@placeholder='Type a comment']"
    send_button = "//button[contains(text(),'Send')]"


    # C27838 Deal changing status

    '''
     Preconditions

    User should be on deal details screen
    Steps
    
    1.Click on More icon "..."
    2.Click on any of the displayed option
    3.Click on Closed option
    4.Click on Submit button from confirmation box
    Expected Result
    
    Deal's status should get changed to Closed and it should get reflected on deal details screen
     
    '''

    menu_icon = ".sc-1dok22n-0 > path"
    click_closed = "//p[contains(text(),'Closed')]"
    submit_button = "//button[contains(text(),'Submit')]"
    after_closed_tag = "//p[contains(text(),'Closed')]"

    def SubmitButton(self):
        self.elementClick(self.submit_button)

    def ClickMenuIcon(self):
        self.elementClick(self.menu_icon, locatorType='css')

    def DealChangingStatus(self):
        time.sleep(2)
        self.ClickMenuIcon()
        time.sleep(2)
        self.elementClick(self.click_closed)
        time.sleep(2)
        self.SubmitButton()
        time.sleep(2)
        reactivate = self.getText(self.after_closed_tag)
        reactivate_text = "Closed"
        self.verifyTextContains(actualText=reactivate, expectedText=reactivate_text)


    # C27839 Location, Walkscore & Google place amenities

    '''
     Preconditions
    
    User should be on deal details screen
    Steps
    
    1.Scroll down the details screen
    2.Click on Load button
    Expected Result
    
    Location of the deal should get displayed above map section
    - Walkscore details should get displayed left to map section in right side
    - Google place amenities should get displayed below map section as "Nearby bussiness"
     
        
    '''

    scroll_to_location = "//h4[contains(text(),'Location')]"
    load_button = "//button[contains(text(),'Load')]"
    near_by_business = "//p[contains(text(),'Restaurants')]"
    near_by_business_fitness = "//p[contains(text(),'Fitness')]"

    def LocationScreenGoogle(self):
        time.sleep(2)
        self.innerScrollUp(self.scroll_to_location)
        time.sleep(2)
        self.elementClick(self.load_button)
        time.sleep(2)
        restaurant = self.getText(self.near_by_business)
        restaurant_text = "Restaurants"
        fitness = self.getText(self.near_by_business_fitness)
        fitness_text = "Fitness"
        self.verifyTextContains(actualText=restaurant, expectedText=restaurant_text)
        self.verifyTextContains(actualText=fitness, expectedText=fitness_text)


    # C33433 Button/link to create deal at existing location/place

    '''
     Preconditions

    User should be on deal details screen
    Steps
    
    1.Click on More icon
    2.Click on + Add new deal button from modal box
    3.Click on Add button from pop-up box
    Expected Result
    
    New deal should get created
    Newly created deal's detail screen should get displayed
    Old already available deal should have its deal number get displayed i.e. Deal 1/Deal 2/ ..
    
        
    
    1.Click on + Add new deal link displayed below Other deals at this property
    2.Click on Add button from pop-up box
    
    Note : This link will only get enabled once there are other deals available to that property
    Expected Result
    
    New deal should get created
    Newly created deal's detail screen should get displayed
    Old already available deal should have its deal number get displayed i.e. Deal 1/Deal 2/ 
    
    '''

    add_new_deal = "//p[contains(text(),'Add new deal at this location')]"
    click_add_button = "//button[contains(text(),'Add')]"
    deal_tag = "//p[contains(.,'Deal 2')]"

    def CreateDealFromExistingDeal(self):
        time.sleep(2)
        self.innerScrollUp(self.menu_icon, locatorType='css')
        time.sleep(2)
        self.elementClick(self.menu_icon, locatorType='css')
        time.sleep(2)
        self.elementClick(self.add_new_deal)
        time.sleep(2)
        self.elementClick(self.click_add_button)
        time.sleep(5)
        deal_tag_name = self.getText(self.deal_tag)
        tag_name = "Deal 2"
        self.verifyTextContains(actualText=deal_tag_name, expectedText=tag_name)


    add_deal_from_created_deal = "//p[contains(.,'+ Add new deal at this location')]"
    deal_tag1 = "//p[contains(.,'Deal 3')]"

    def AddDealFromCreatedDeal(self):
        time.sleep(2)
        self.elementClick(self.add_deal_from_created_deal)
        time.sleep(2)
        self.elementClick(self.click_add_button)
        time.sleep(2)
        deal_tag_name = self.getText(self.deal_tag1)
        tag_name = "Deal 3"
        self.verifyTextContains(actualText=deal_tag_name, expectedText=tag_name)



    # C39538 Deal details > Performance tab

    '''
     Steps
    1

    "GrossConstructionCost field exists in the Performance tab"
    1.Click on any deal
    2.Click on the Performance tab.
    Expected Result
    
    A field called Gross Construction Cost is available on the Performance Tab after 'Adjusted NPV' and before 'Annual Escalations'.
    2
        
    "GrossConstructionCost field is editable by the user"
    1.Open a deal from stage C or later
    2.Open the Performance tab
    3.Edit the gross construction cost
    Expected Result
    
    The old value no longer shows and the new value is persisted on the page, even after reload.
    
    '''

    gross_text = "//span[contains(text(),'Gross Construction Cost')]"

    def GrossConstructionCostONPerformanceTab(self):
        time.sleep(2)
        self.innerScroll(self.scroll_to_general_tab)
        time.sleep(2)
        self.elementClick(self.click_performance_tab)
        time.sleep(2)
        verify_gross_text = self.getText(self.gross_text)
        verify_text = "Gross Construction Cost"
        self.verifyTextContains(actualText=verify_gross_text, expectedText=verify_text)

    click_closed_tag_to_back_to_deal1 = "//p[contains(.,'Closed')]"
    check_gross_value = "//li[7]//span[2]"

    def GrossConstructionFieldEditable(self):
        time.sleep(2)
        self.elementClick(self.click_closed_tag_to_back_to_deal1)
        time.sleep(4)
        self.innerScroll(self.scroll_to_general_tab)
        time.sleep(2)
        self.elementClick(self.click_performance_tab)
        time.sleep(2)
        self.elementClick(self.click_to_open_performance_tab)
        time.sleep(2)
        grossconstructioncost = "300000"
        self.EnterGrossConstructionCost(grossconstructioncost)
        time.sleep(2)
        self.elementClick(self.click_Save_button)
        time.sleep(4)
        g_value = self.getText(self.check_gross_value)
        g_value = g_value.replace("$", '')
        g_value = g_value.replace(",", '')
        self.verifyTextContains(actualText=g_value, expectedText=grossconstructioncost)










































