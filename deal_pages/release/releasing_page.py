import time
import datetime
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from selenium.webdriver.common.keys import Keys


class ReleasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.driver = driver

    # C27840 Release E>D

    '''
    Preconditions

    User should be on deal details screen
    Steps
    
    1.Click on Release to D button
    2.Add Real estate manger in the first field of E>D modal box
    3.Select any Product type from the drop-down menu
    4.Click on Desks field and its value
    5.Click on RSF field and its value
    6.Add Est. C release date from calendar view
    7.Add Possession date from calendar view
    8.Select region
    9.Select territory
    10.Check Tour completed? field
    11.Click on Submit button
    Expected Result
    
    Deal should get released to stage D

    '''

    release_to_d_button = "//span[contains(text(),'Release to D')]"
    enter_value_real_state_manager = "//input[@placeholder='Enter a name']"
                                    #= "//div[@id='app']/div/div[2]/div/div/div/div/div/div[2]/div/div/div/input"
    #select_value_real_state_manager = "//li[contains(.,'Gaurav Dave')]"
    select_value_real_state_manager = "//li[2]/p"
    enter_desk = "//input[@name='desks']"
    enter_rsf = "//input[@name='rsf']"
    est_c_release_calendar = "//input[@id='estimatedReleaseFromDToCDate']"
    possession_date = "//input[@id='possessionDate']"
    add_floor_button_after_release = "//span[contains(text(),'Add floors')]"

    '''
    
    import datetime
    base = datetime.datetime.now()
    for x in range(0, 3):
      a = (base + datetime.timedelta(days=x))
      print(a.strftime("%m/%d/%Y"))
      
    '''

    def ReleaseToDButton(self):
        self.elementClick(self.release_to_d_button)

    def EnterRealStateManager(self, name): # enter real state manager value.
        self.elementClick(self.enter_value_real_state_manager)
        time.sleep(2)
        self.sendKeys(name, self.enter_value_real_state_manager)

    def EnterCRelease(self, toDate): # Enter to date
        self.elementClick(self.est_c_release_calendar)
        time.sleep(2)
        self.sendKeys(toDate, self.est_c_release_calendar)

    def EnterPossession(self, possessionDate): # Enter possession date
        self.elementClick(self.possession_date)
        time.sleep(2)
        self.sendKeys(possessionDate, self.possession_date)

    '''
    
    Steps:
    1. Used add deal function wrriten in deal deal page and created a deal
    2. Clicked on release to d button
    3. Add Real estate manger in the first field of E>D modal box
    3. Select any Product type from the drop-down menu
    4. Click on Desks field and its value
    5. Click on RSF field and its value
    6. Add Est. C release date from calendar view
    7. Add Possession date from calendar view
    8. Select region
    9. Select territory
    10. Check Tour completed? field
    11. Click on Submit button
    
    '''

    add_broker_button = "//button[contains(text(),'Add/edit broker')]"
    add_broker_link = "//p[contains(.,'+ Add broker')]"
    broker_textbox1 = "//div[@id='app']/div/div[2]/div[2]/div/div/div/div/div/div/div/div/input"
    select_broker = "//p[contains(.,'Gaurav Dave')]"

    def EnterBroker(self, brokername):
        self.elementClick(self.broker_textbox1)
        time.sleep(2)
        self.sendKeys(brokername, self.broker_textbox1)

    def EnterBrokerValueByClickingAddEditBrokerButton(self):
        self.elementClick(self.add_broker_link)
        brokername = "Gaurav dave"
        self.EnterBroker(brokername)
        time.sleep(2)
        self.elementClick(self.select_broker)
        time.sleep(2)
        self.elementClick(self.dealdetail.click_team_save_button)
        time.sleep(2)

    def ReleaseEToD(self):
        time.sleep(2)
        self.deal.AddNewDeal()
        time.sleep(4)
        self.ReleaseToDButton()
        time.sleep(2)
        name = "Gaurav Dave"
        self.EnterRealStateManager(name)
        time.sleep(2)
        self.elementClick(self.select_value_real_state_manager)
        time.sleep(2)
        self.elementClick(self.add_broker_button)
        time.sleep(2)
        self.EnterBrokerValueByClickingAddEditBrokerButton()
        time.sleep(2)
        num = '100'
        self.dealdetail.EnterDeskValue(num)
        time.sleep(2)
        rsfnum = '100'
        self.dealdetail.EnterRSFValue(rsfnum)
        time.sleep(2)
        self.dateSelection()
        time.sleep(5)
        self.dealdetail.CheckLabelYes()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(2)
        add_floor = "Update floors"
        addFloor = self.getText(self.temp_update_floor_button)
        self.verifyTextContains(actualText=addFloor, expectedText=add_floor)

    # Date selection method created to enter date for possession and opening date

    def dateSelection(self):
        base = datetime.datetime.now()
        for x in range(1, 3):
            if x == 1:
                a = (base + datetime.timedelta(days=x))
                a = (a.strftime("%m/%d/%Y"))
                self.log.info(a)
                self.EnterCRelease(a)
            else:
                a = (base + datetime.timedelta(days=x))
                a = (a.strftime("%m/%d/%Y"))
                self.log.info(a)
                time.sleep(2)
                self.EnterPossession(a)


    # Add Floor by clicking on Add Floor button
    # Enter all the values and click on save button

    temp_update_floor_button = "//span[contains(text(),'Update floors')]"
    button_request_release_to_c = "//span[contains(text(),'Request release')]"

    def ClickButtonReleaseToC(self):
        self.elementClick(self.button_request_release_to_c)

    def AddFloors(self):
        time.sleep(3)
        self.elementClick(self.temp_update_floor_button)
        time.sleep(2)
        # self.elementClick(self.temp_update_floor_button)
        # time.sleep(2)
        self.dealdetail.EnteringFloorValues()
        time.sleep(2)
        verify_button = self.getText(self.button_request_release_to_c)
        verify_button_text = "Request release"
        self.verifyTextContains(actualText=verify_button, expectedText=verify_button_text)


    # C27841 Release D>C

    '''
    
    Preconditions
    
    User should be on deal details screen having stage D
    Floors info is added on deal
    Steps
    
    1.Click on Release to C button
    2.Click on Add file Excel link for adding FiMo file
    3.Select proper excel file
    4.Click on Next button
    5.Add description of the deal
    6.Select market if not selected
    7.Add Landlord name in landlord name field
    8.Add Landlord email id in landlord contract field
    9.Click on Next button
    10.Add approver name in the field
    11.Approve the request if you are approver from deal details screen
    Expected Result
    
    Deal should get released to stage C

    '''

    add_fimo_link_text = "Add file (Excel)"
    #upload_next_button_step1 = "//div[@id='app']/div/div[2]/div/div/div/div/div/div[4]/div[2]/button"
    next_button_step2 = "//div[2]/div[3]/button"
    upload_next_button_step1 = "//div[@class='button--wrapper wdunhr-0 kUWJWD']//button[@class='button--button'][contains(text(),'Next')]"
    description_field = "//textarea[@placeholder='Describe the deal']"
    click_add_edit_landlord = "//button[contains(text(),'Add/edit landlord')]"
    enter_landlord_name = "//input[@placeholder='Company name']"
    select_landlord = "//p[contains(.,'Gunners')]"
    click_save_button = "//span[contains(text(),'Save')]"
    enter_approver = "//div[1]/div/div[2]/div/div/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div/input"
    select_approver = "//li[2]/p"
    request_change_button_for_verification = "//span[contains(text(),'Request changes')]"
    approve_release_button = "//span[contains(text(),'Approve release')]"
    click_approve_button = "//div[@id='app']/div/div[2]/div/div/div/div/div/div[2]/button/span"

    def ClickApproveButtonAfterMovingFromXtoY(self):
        self.elementClick(self.approve_release_button)

    def ClickNextButton(self):
        time.sleep(5)
        self.elementClick(self.upload_next_button_step1)

    def ClickSaveButton(self):
        self.elementClick(self.click_save_button)

    def EnterDescriptionRelease(self, desc):
        self.elementClick(self.description_field)
        time.sleep(1)
        self.sendKeys(desc, self.description_field)

    def EnterLandlordName(self, name):
        self.elementClick(self.enter_landlord_name)
        time.sleep(2)
        self.sendKeys(name, self.enter_landlord_name)

    def AddApprover(self, approver_name):
        self.elementClick(self.enter_approver)
        time.sleep(2)
        self.sendKeys(approver_name, self.enter_approver)

    def AddFileMemoSheet(self):
        self.elementClick(self.add_fimo_link_text, locatorType='link')
        time.sleep(2)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/v4.2_Proforma(1).xlsb"
        self.dealdetail.UploadDocuments(doc)

    def ApproveReleaseButtonClick(self):
        self.elementClick(self.approve_release_button)
        time.sleep(3)
        self.elementClick(self.click_approve_button)

    def SelectLandlordFromAddEditButton(self):
        time.sleep(2)
        self.elementClick(self.click_add_edit_landlord)
        time.sleep(2)
        name = 'gunner'
        self.EnterLandlordName(name)
        time.sleep(2)
        self.elementClick(self.select_landlord)
        time.sleep(2)
        self.ClickSaveButton()


    def ReleaseDToCForm(self):
        time.sleep(2)
        self.elementClick(self.button_request_release_to_c)
        time.sleep(2)
        self.AddFileMemoSheet()
        time.sleep(45)
        self.log.info("hiiii pass")
        self.ClickNextButton()
        time.sleep(2)
        desc = "Running automation release from D - C"
        self.EnterDescriptionRelease(desc)
        self.SelectLandlordFromAddEditButton()
        time.sleep(2)
        self.elementClick(self.next_button_step2)
        time.sleep(2)
        approver_name = 'Gaurav Dave'
        self.AddApprover(approver_name)
        time.sleep(2)
        self.elementClick(self.select_approver)
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(8)
        verify_deal_after_completion = self.getText(self.request_change_button_for_verification)
        text_verify = "Request changes"
        self.verifyTextContains(actualText=verify_deal_after_completion, expectedText=text_verify)

    def ReleaseDToC(self):
        self.ReleaseDToCForm()
        self.ApproveReleaseButtonClick()

    # C27842 Release C>B

    '''
    
    Preconditions

    User should be on deal details screen having stage C
    Floors info is added on deal
    Steps
    
    1.Click on Release to B button
    2.Click on Add file link of Deal Memo field
    3.Select deal memo file and upload it
    4.Click on Add file link of Term sheet field
    5.Select Term sheet file and upload it
    6.Click on Add file link of Financial model field
    7.Select FiMo file and upload it
    8.Click on Next button
    9.Confirm deal team members by adding members in each field
    10.Click on Next button after adding members
    11.Add regional approver(user can add his name also in the field)
    12.Click on Submit button, after confirming global approver
    13.Ask approvers to approve the request
    Expected Result
    
    Deal should get released to stage B

    '''

    button_request_release_to_b = "//span[contains(text(),'Request release')]"
    add_termsheet = "Add file (PDF, Doc)"
    add_deal_memo = "Add file (PDF)"
    select_date_leasing_sign = "//input[@id='date']"
    add_additional_financial_model = "//div[4]//p[2]//a[1]"

    def AddTermSheet(self):
        self.elementClick(self.add_termsheet, locatorType='link')
        time.sleep(2)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/1.pdf"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(10)

    def AddDealMemo(self):
        self.elementClick(self.add_deal_memo, locatorType='link')
        time.sleep(2)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/DealMemo.pdf"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(20)

    def AddAdditionalFinancialModelPDf(self):
        self.elementClick(self.add_additional_financial_model)
        time.sleep(2)
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/1.pdf"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(15)

    def EnterLeaseSigningDate(self, leasesign):
        self.elementClick(self.select_date_leasing_sign)
        time.sleep(2)
        self.sendKeys(leasesign, self.select_date_leasing_sign)

    def ReleaseProcessCTOB(self):
        time.sleep(3)
        self.elementClick(self.button_request_release_to_b)
        time.sleep(2)
        self.AddFileMemoSheet()
        time.sleep(35)
        self.AddDealMemo()
        self.AddTermSheet()
        self.AddAdditionalFinancialModelPDf()
        time.sleep(2)
        self.ReleaseProcessCtoBStep2()

    def ReleaseProcessCtoBStep2(self):
        self.elementClick(self.upload_next_button_step1)
        time.sleep(2)
        base = datetime.datetime.now()
        for x in range(1, 2):  # adding method to select lease signing date
            if x == 1:
                a = (base + datetime.timedelta(days=x))
                a = (a.strftime("%m/%d/%Y"))
                self.log.info(a)
                self.EnterLeaseSigningDate(a)
        time.sleep(2)
        self.dealdetail.SelectTransactionManager()
        time.sleep(2)
        self.dealdetail.SelectRealStateAnalystValue()
        time.sleep(2)
        self.dealdetail.SelectSourcer()
        #time.sleep(2)
        #self.dealdetail.SelectInternalCounsel()
        #time.sleep(2)
        self.elementClick(self.next_button_step2)
        time.sleep(2)
        name = "Gaurav Dave"
        self.EnterRealStateManager(name)
        self.elementClick(self.select_value_real_state_manager)
        time.sleep(2)

    # Global approvers do not exist on C>B deals

    '''
    
    "In C>B release request, user cannot add global approvers"

    Navigate to deal in stage C
    Click CTA to “Request release to B (Leasing)”
    Upload all required docs and click next
    Enter all deal team member slots and click next
    
    Expected :
    
    On “Add approvers” section, “Global committee” section should not have options to add users and should read “Global Approvers are not required for C>B deals”
    “Regional committee” section should have ability to add approvers
    
    '''

    global_approver_text_on_popup = "//p[contains(text(),'Global Approvers are not required for C>B deals')]"

    def VerifyGlobalApproversDoNotExistOnCToBDeals(self):
        self.ReleaseProcessCTOB()
        ### not required now as per the new flow
        #$text = "Global Approvers are not required for C>B deals"
        #globe_text = self.getText(self.global_approver_text_on_popup)
        #self.verifyTextContains(actualText=text, expectedText=globe_text)

    # adding meeting note method

    add_meeting_notes_button = "//span[contains(text(),'Add meeting notes')]"
    enter_meeting_notes = "//textarea[@placeholder='Enter text here']"
    enter_meeting_date = "//input[@id='regionalCommitteeMeetingDate']"
    enter_time = ".tdxc9i-0"

    def AddMeetingNoteButton(self):
        self.elementClick(self.add_meeting_notes_button)

    def EnterMeetingNote(self, text):
        self.elementClick(self.enter_meeting_notes)
        time.sleep(2)
        self.sendKeys(text, self.enter_meeting_notes)

    def EnterMeetingDate(self, a):
        self.elementClick(self.enter_meeting_date)
        time.sleep(2)
        base = datetime.datetime.now()
        a = (base + datetime.timedelta())
        a = (a.strftime("%m/%d/%Y"))
        self.log.info(a)
        self.sendKeys(a, self.enter_meeting_date)

    def EnterTime(self, tt):
        time.sleep(2)
        self.sendKeys(tt, self.enter_time, locatorType='css')

    def PressArrowKey(self, value):
        self.sendKeys(value, self.enter_time, locatorType='css')

    def AddMeetingNote(self):
        time.sleep(2)
        self.elementClick(self.add_meeting_notes_button)
        self.EnterValueInMeetingNotesModalBox()
        self.ClickSaveButton()

    def EnterValueInMeetingNotesModalBox(self):
        time.sleep(2)
        text = 'This is automatic meeting notes'
        self.EnterMeetingNote(text)
        time.sleep(2)
        base = datetime.datetime.now()
        a = (base + datetime.timedelta())
        a = (a.strftime("%m/%d/%Y"))
        self.log.info(a)
        self.EnterMeetingDate(a)
        time.sleep(2)
        tt = "1212PM"
        self.elementClick(self.enter_time, locatorType='css')
        self.PressArrowKey(Keys.ARROW_LEFT)
        self.PressArrowKey(Keys.ARROW_LEFT)
        self.EnterTime(tt)
        time.sleep(2)

    def ReleaseCToB(self):
        self.dealdetail.SubmitButton()
        time.sleep(4)
        self.ApproveReleaseButtonClick()
        time.sleep(4)
        self.AddMeetingNote()
        time.sleep(3)
        button = self.getText(self.move_to_b_button)
        button_text = "Release to B"
        self.verifyTextContains(actualText=button, expectedText=button_text)


    move_to_b_button = "//span[contains(text(),'Release to B')]"
    button_release = "//button[contains(text(),'Release')]"
    release_to_a_button = "//span[contains(text(),'Request release')]"

    def ReleaseMoveToB(self):
        time.sleep(2)
        self.elementClick(self.move_to_b_button)
        time.sleep(2)
        self.deal.SelectFirstDateFromCalendar()
        time.sleep(4)
        base = datetime.datetime.now()
        for x in range(1, 2):  # adding method to select lease signing date
            if x == 1:
                a = (base + datetime.timedelta(days=x))
                a = (a.strftime("%m/%d/%Y"))
                self.log.info(a)
                self.EnterLeaseSigningDate(a)
        time.sleep(2)
        self.elementClick(self.button_release)
        #time.sleep(3)
        #button = self.getText(self.release_to_a_button)
        #button_text = "Request release"
        #self.verifyTextContains(actualText=button, expectedText=button_text)


    approver_1 = "//div[3]/div/div/div/div[1]/div/div/input"
    approver_2 = "//div[3]/div/div/div/div[2]/div/div/input"
    approver_4 = "//div[3]/div/div/div/div[4]/div/div/input"
    close_icon = ".icon--close"
    select_value_real_state_manager_dhiraj = "//li[contains(.,'Dhiraj')]"

    def EnterApprover1(self, app1):
        self.elementClick(self.approver_1)
        time.sleep(2)
        self.sendKeys(app1, self.approver_1)

    def EnterApprover2(self, app2):
        self.elementClick(self.approver_2)
        time.sleep(2)
        self.sendKeys(app2, self.approver_2)

    def EnterApprover4(self, app4):
        self.elementClick(self.approver_4)
        time.sleep(2)
        self.sendKeys(app4, self.approver_4)

    def ClickCloseIcon(self):
        self.elementClick(self.close_icon, locatorType='css')

    def ReleasePopUpFieldEntry(self):
        time.sleep(2)
        self.elementClick(self.release_to_a_button)
        time.sleep(2)
        self.AddFileMemoSheet()
        time.sleep(45)
        self.AddDealMemo()
        time.sleep(2)
        self.AddTermSheet()
        time.sleep(2)
        self.AddAdditionalFinancialModelPDf()
        self.ClickNextButton()
        time.sleep(2)
        self.elementClick(self.next_button_step2)
        time.sleep(2)
        app1 = "Gaurav Dave"
        self.EnterApprover1(app1)
        self.elementClick(self.select_value_real_state_manager)
        time.sleep(2)
        # self.ClickCloseIcon()
        # app2 = "Gaurav Dave"
        # self.EnterApprover2(app2)
        # self.elementClick(self.select_value_real_state_manager)
        time.sleep(2)
        app4 = "Gaurav Dave"
        self.EnterApprover4(app4)
        time.sleep(2)
        self.elementClick(self.select_value_real_state_manager)

    def ReleaseToA(self):
        self.ReleasePopUpFieldEntry()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(2)
        self.ApproveReleaseButtonClick()



