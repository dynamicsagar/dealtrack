import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.release.releasing_page import ReleasePage


class UnReleasePages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.release = ReleasePage(self.driver)
        self.driver = driver


    # C27844 Unrelease D>E

    '''
    
     Preconditions

    User should be on deal details screen having stage D
    Steps
    
    1.Click on More icon "..." displayed on top-right corner of the screen
    2.Click on Move back to E(Discovery) button from modal box
    3.Click on Submit button from confirmation box
        
    '''

    select_sourcing = "//div[5]/div/div/div[2]/div[2]/div/img"
    select_term_sheet = "//div[5]/div/div/div[2]/div[4]/div/img"
    select_c_to_b = "//div[5]/div/div/div[2]/div[5]/div/img"
    select_leasing = "//div[5]/div/div/div[2]/div[6]/div/img"
    click_move_back_to_E = "//p[contains(text(),'Move back to ')]"
    reset_button = "//button[contains(text(),'Reset')]"
    select_lease_signed = "//div[5]/div/div/div[2]/div[8]/div/img"

    def ClickResetButton(self):
        time.sleep(2)
        self.elementClick(self.reset_button)

    def SelectSourcing(self):
        time.sleep(2)
        self.elementClick(self.select_sourcing)

    def GlobalFilterSelection(self):
        self.deal.MoreFilterIcon()
        self.ClickResetButton()
        time.sleep(2)
        self.deal.ClickStageField()

    def ClickMenuIcon(self):
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.dealdetail.ClickMenuIcon()
        time.sleep(3)
        self.elementClick(self.click_move_back_to_E)
        time.sleep(3)
        self.dealdetail.SubmitButton()

    def UnreleaseDTOE(self):
        self.deal.ClickBackArrow()
        time.sleep(2)
        self.GlobalFilterSelection()
        time.sleep(2)
        self.elementClick(self.select_sourcing)
        time.sleep(2)
        self.ClickMenuIcon()
        time.sleep(3)
        text = self.getText(self.release.release_to_d_button)
        button_text = "Release to D"
        self.verifyTextContains(actualText=text, expectedText=button_text)


    # C27845  Unrelease C>D

    '''
    
    Preconditions

    User should be on deal details screen having stage C
    Steps
    
    1.Click on More icon "..." displayed on top-right corner of the screen
    2.Click on Move back to D(Sourcing) button from modal box
    3.Click on Submit button from confirmation box
    Expected Result
    
    Deal should get unreleased from stage C to D & an Email should be sent to all the deal team members
    
    '''

    # def PressBackArrow(self, key):
    #     self.elementClick(self.deal.ClickStageField())
    #     time.sleep(2)
    #     self.sendKeys(key, self.deal.ClickStageField())

    def ClickReset(self):
        self.elementClick(self.reset_button)

    def UnReleaseCTOD(self):
        self.GlobalFilterSelection()
        time.sleep(2)
        self.elementClick(self.select_term_sheet)
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.ClickMenuIcon()
        time.sleep(4)
        text = self.getText(self.release.button_request_release_to_c)
        button_text = "Request release"
        self.verifyTextContains(actualText=text, expectedText=button_text)

    # C27846 Unrelease B>C

    '''
    
     Preconditions

    User should be on deal details screen having stage B
    Steps
    
    1.Click on More icon "..." displayed on top-right corner of the screen
    2.Click on Move back to C(Term Sheet) button from modal box
    3.Click on Submit button from confirmation box
    Expected Result
    
    Deal should get unreleased from stage B to C & an Email should be sent to all the deal team members
    
    '''

    def UnReleaseBTOC(self):
        time.sleep(2)
        self.GlobalFilterSelection()
        time.sleep(2)
        self.elementClick(self.select_leasing)
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.ClickMenuIcon()
        time.sleep(4)
        text = self.getText(self.release.button_request_release_to_b)
        button_text = "Request release"
        self.verifyTextContains(actualText=text, expectedText=button_text)

    # C27847 Unrelease A>B

    '''
    
     Preconditions

    User should be on deal details screen having stage A
    Steps
    
    1.Click on More icon "..." displayed on top-right corner of the screen
    2.Click on Move back to B(Leasing) button from modal box
    3.Click on Submit button from confirmation box
    Expected Result
    
    Deal should get unreleased from stage A to B & an Email should be sent to all the deal team members
        
    '''

    button_release_to_a = "//span[contains(text(),'Request release')]"

    def UnReleaseATOB(self):
        time.sleep(2)
        self.GlobalFilterSelection()
        time.sleep(2)
        self.elementClick(self.select_lease_signed)
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.ClickMenuIcon()
        time.sleep(4)
        text = self.getText(self.button_release_to_a)
        button_text = "Request release"
        self.verifyTextContains(actualText=text, expectedText=button_text)


    # C39536 Budget as new required doc while releasing B-A

    '''
    Preconditions

    User should be logged into the app
    Steps
    
    "Additional required document to be uploaded"
    1.Click on any deal having stage B
    2.Click on Release to stage A button
    
    Expected : 
    1.Request release B-> A modal box should get invoked & new optional document field as "Budget" should be displayed on it
    2.Document should have a optional tag near it
    3.Document should in excel format
    4.It should be displayed in the same way the other release documents do

    '''

    add_budget_file = "//div[5]//p[2]//a[1]"
    optional_tag = "//p[contains(text(),'optional')]"
    verify_added_file = "//p[contains(text(),'1 file added')]"
    verify_error_msg = "//div[@id='__filestack-picker']/div/div[2]/div"
    upload_pop_up_close = ".fsp-picker__close-button"

    def AddBudgetFile(self):
        self.elementClick(self.add_budget_file)
        time.sleep(2)

    def BudgetAsNewRequiredDocWhileReleasingBToA(self):
        time.sleep(2)
        self.GlobalFilterSelection()
        time.sleep(2)
        self.elementClick(self.select_leasing)
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.elementClick(self.button_release_to_a)
        time.sleep(3)
        self.AddBudgetFile()
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/v4.2_Proforma(1).xlsb"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(45)
        text = self.getText(self.verify_added_file)
        original_text = "1 file added; 4 remaining"
        self.verifyTextContains(actualText=text, expectedText=original_text)

    # upload the document and click on cancel button
    cancel_button_on_popup = "//button[contains(text(),'Cancel')]"

    def VerifyByUploadRequiredDocAndCancelTheProcess(self):
        time.sleep(2)
        self.elementClick(self.cancel_button_on_popup)
        time.sleep(2)
        text = self.getText(self.button_release_to_a)
        button_text = "Request release"
        self.verifyTextContains(actualText=text, expectedText=button_text)

    # upload invalid documents and verify the error message.

    def BudgetAsNewRequiredDocWhileReleasingBToA_VerifyInvalidFileUpload(self):
        time.sleep(2)
        self.elementClick(self.button_release_to_a)
        time.sleep(2)
        self.AddBudgetFile()
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/1.pdf"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(2)
        text = self.getText(self.verify_error_msg)
        error_text = "File 1.pdf is not an accepted file type. The accepted file types are .xls,.xlsx,.xlsm,.xlsb"
        self.verifyTextContains(actualText=text, expectedText=error_text)


    # C54649 Lease document validation

    '''
    
    Preconditions

    User should be logged in
    Steps
    
    "Uploading lease document informs user of access control"
    1.Find or create deal that is stage B
    2.Create release request
    3.When uploading documents begin to upload lease

    Expected Result
    There exists text that informs the user that lease documents will not be viewable on Dealtrack after submission
    
    '''

    lease_text = "//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div[9]/div[2]/div[4]/div[2]/span"
    lock_icon = ".Regular-sc-ju30to svg"
    lease_text_on_popup = "//p[contains(text(),'will not be accessible from application')]"

    def VerifyLeaseTextOnPopUp(self):
        time.sleep(2)
        self.elementClick(self.upload_pop_up_close, locatorType='css')
        time.sleep(2)
        text = self.getText(self.lease_text_on_popup)
        text_to_verify = "will not be accessible from application"
        self.verifyTextContains(actualText=text, expectedText=text_to_verify)

    '''
    
    "Lease document from cancelled release request is not viewable"
    1.Find or create deal in stage B
    2.Create release request to A
    3.Add approvers and upload documents
    4.Cancel release request
    
    Expected :
    Lease approval document has moved to "Attachments" section but is dimmed and locked
    Clicking on document does nothing
    
    '''

    scroll_to_documents = "//a[contains(text(),'Documents')]"


    def VerifyLeaseAttachementByClickingLeaseDocument(self):
        time.sleep(2)
        self.elementClick(self.cancel_button_on_popup)
        time.sleep(2)
        self.release.ReleasePopUpFieldEntry()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(3)
        self.elementClick(self.scroll_to_documents)
        time.sleep(2)
        self.elementClick(self.lock_icon, locatorType='css')
        time.sleep(2)
        financial_text = self.getText(self.scroll_to_documents)
        text = 'Documents'
        self.verifyTextContains(actualText=text, expectedText=financial_text)

    # C54915 Global approvers do not exist on C>B deals

    '''
     Preconditions

    Log in to dealtrack
    
    Steps:
    "On C>B deals, global approvers section shows copy instead of approvers list"
    Navigate to deal in C>B stage
    
    Expected : 

    Under approvers section, “Global approvers” bucket should not have any users listed out and should read “Global Approvers are not required for C>B deals”
    Regional approvers should be listed as normal

    '''

    global_approver_c_to_b = "//p[contains(text(),'Global Approvers are not required for C>B deals')]"


    # def VerifyGlobalApproverNotExistOnCtoBDeals(self):
    #     time.sleep(2)
    #     self.GlobalFilterSelection()
    #     time.sleep(2)
    #     self.elementClick(self.select_c_to_b)
    #     time.sleep(2)
    #     self.deal.ClickApplyButton()
    #     time.sleep(2)
    #     self.innerScroll(self.dealdetail.scroll_to_team)
    #     time.sleep(2)
    #     g_approver = self.getText(self.global_approver_c_to_b)
    #     g_approver_text = "Global Approvers are not required for C>B deals"
    #     self.verifyTextContains(actualText=g_approver, expectedText=g_approver_text)









































