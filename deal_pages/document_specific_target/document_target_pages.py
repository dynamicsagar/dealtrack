import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.release.releasing_page import ReleasePage
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.request_revision.request_revision_pages import RequestRevisionPages


class DocumentSpecificPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deall = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.release = ReleasePage(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.request = RequestRevisionPages(self.driver)
        self.driver = driver


    # C63079 Document View

    """
    
    Preconditions

    User is logged into dealtrack
    Create a new deal by clicking on the (+) on the bottom left side of the page, Add an address and Click Add

    Steps

    Scroll below General info tab
    
    Expected Result

    'Documents' section is displayed with the following associated tags in this order (Financial model, term sheet, deal memo, lease first then the rest in alphabetical order)
    1. Financial Model
    2. Term Sheet
    3. Deal Memo
    4. Lease
    5. Budget
    6. Ops Rider
    7. Programming package (pkg)
    8. Project schedule
    9. Test Fit
    10. RevOps FiMo
    
    Below the associated file tag you have a grey thumbnail with a (+) icon in the center

    Below target tags there is an 'Other attachments' section with a (+) icon next to it to upload attachments.
    
    Depending on side of the page the documents thumbnail displays will shift, if screen is wide enough all the target tags will be on one row, number of rows increase depending on how small the screen is but the size of the thumbnail does not change


    """

    scroll_to_documents = "//a[contains(text(),'Documents')]"
    financial_model = "//span[contains(text(),'Financial model')]"
    deal_memo = "//span[contains(text(),'Deal memo')]"
    lease = "//span[contains(text(),'Lease')]"
    budget = "//span[contains(text(),'Budget')]"
    ops_rider = "//span[contains(text(),'Ops rider')]"
    programing_pkg = "//span[contains(text(),'Programming pkg')]"
    project_schedule = "//span[contains(text(),'Project schedule')]"
    revops = "//span[contains(text(),'RevOps FiMo')]"
    testFit = "//span[contains(text(),'Test fit')]"


    def Scroll_to_documents(self):
        self.elementClick(self.scroll_to_documents)

    def VerifyDocumentView(self):
        time.sleep(2)
        self.deall.ClickBackArrow()
        time.sleep(2)
        self.deall.AddNewDeal()
        time.sleep(2)
        self.Scroll_to_documents()
        time.sleep(2)
        self.elementPresenceCheck(self.deal_memo, byType='xpath')
        self.elementPresenceCheck(self.financial_model, byType='xpath')
        self.elementPresenceCheck(self.lease, byType='xpath')
        self.elementPresenceCheck(self.budget, byType='xpath')
        self.elementPresenceCheck(self.ops_rider, byType='xpath')
        self.elementPresenceCheck(self.programing_pkg, byType='xpath')
        self.elementPresenceCheck(self.project_schedule, byType='xpath')
        self.elementPresenceCheck(self.revops, byType='xpath')
        self.elementPresenceCheck(self.testFit, byType='xpath')


    # Specific target tag upload view

    '''
    
    Preconditions

    User is logged into dealtrack
    User has created a new deal and is in stage E: (https://wework.testrail.net/index.php?/cases/view/59784 )
    
    Upload each documents one by one. 


    '''
    click_new_financial_model = ".sc-12w36a0-0:nth-child(2) svg"
    click_lease_upload_pdf = ".sc-12w36a0-0:nth-child(5) svg"
    click_budget_upload_xls = ".sc-12w36a0-0:nth-child(6) svg"
    click_ops_rider_upload_pdf = ".sc-12w36a0-0:nth-child(7) svg"
    click_programing_pkg_upload_pdf = ".sc-12w36a0-0:nth-child(8) svg"
    click_project_schedule_upload_pdf = ".sc-12w36a0-0:nth-child(9) svg"
    click_revOps_upload_xls = ".sc-12w36a0-0:nth-child(10) svg"
    click_test_fit_upload_pdf = ".sc-12w36a0-0:nth-child(10) svg"
    click_other_attachment_upload_pdf = ".sc-12w36a0-0:nth-child(12) svg"


    def UploadPDF(self):
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/1.pdf"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(15)

    def UploadCSV(self):
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/FiMo.xlsm"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(20)

    def ClickNewFinancialModel(self):
        self.elementClick(self.click_new_financial_model, locatorType='css')
        self.UploadPDF()

    def LeaseUpload(self):
        self.elementClick(self.click_lease_upload_pdf, locatorType="css")
        self.UploadPDF()

    def BudgetUpload(self):
        self.elementClick(self.click_budget_upload_xls, locatorType="css")
        self.UploadCSV()

    def OpsRiderUpload(self):
        self.elementClick(self.click_ops_rider_upload_pdf, locatorType="css")
        self.UploadPDF()

    def ProgramingPkgUpload(self):
        self.elementClick(self.click_programing_pkg_upload_pdf, locatorType="css")
        self.UploadPDF()

    def ProjectScheduleUpload(self):
        self.elementClick(self.click_project_schedule_upload_pdf, locatorType="css")
        self.UploadPDF()

    def RevOpsUpload(self):
        self.elementClick(self.click_revOps_upload_xls, locatorType="css")
        self.UploadCSV()

    def TestFitUpload(self):
        self.elementClick(self.click_test_fit_upload_pdf, locatorType="css")
        self.UploadPDF()

    def OtherAttachmentUpload(self):
        self.elementClick(self.click_other_attachment_upload_pdf, locatorType="css")
        self.UploadPDF()

    def UploadDocumentOneByOne(self):
        time.sleep(2)
        self.dealdetail.TermSheetDocument()
        self.dealdetail.FinacialDocuments()
        self.dealdetail.DealMemo()
        self.ClickNewFinancialModel()
        self.LeaseUpload()
        self.BudgetUpload()
        self.OpsRiderUpload()
        self.ProgramingPkgUpload()
        self.ProjectScheduleUpload()
        self.RevOpsUpload()
        self.TestFitUpload()
        self.OtherAttachmentUpload()


    # Lease target upload

    """
    
    Lease thumbnail has a locked icon and is not viewable and does not download when clicked on
    
    """

    lock_icon = ".Regular-sc-1a1sabl path"

    def LockIcon(self):
        self.getElement(self.lock_icon, locatorType='css')

    def VerifyLockIconAfterUploadingLeaseDocument(self):
        time.sleep(2)
        self.isElementPresent(self.LockIcon())


    # Deal in stage D-C

    '''
    
    Preconditions

    User is logged into dealtrack
    User created/ finds a deal in stage D
    Create a new deal by clicking on the (+) on the bottom left side of the page, Add an address and Click Add, Click release to D (Add release estate manager, Desks, RSF, Est C release date, possession date and press submit)

    Step 	Expected Result
    1 Go to Documents section of deal details page
        
    
    Next to Documents with orange caution icon it says 1 needed
    
    Under target tag Financial Model it says "Upload needed" with an orange caution icon
    
    2 Click on the (+) under financial model and upload a proforma

    Financial model thumbnail says {"D to C release"}{Time: Just now}
    
    Under Financial model tag it says 'Ready for approval''
    
    Next to 'Documents' section it says 'Ready for approval'
    
    3 Click on "Release to C"
    Modal opens and Financial modal has the document that was added on the deal details page under Financial model
    
    4  Enter "edit deal info" details (description, market and landlord)
    
    Add approvers and press submit

    Modal closes (approval buttons appear if you made yourself an approver)
    
    unable to go back and upload any required document, can still cancel release request

    
    '''

    # test_04VerifyDocumentDealInStageDtoC

    text_ready_for_approval = "//div[@id='documents']/div/div/div/div/div[2]"

    def DocumentDealInStageDtoC(self):
        time.sleep(2)
        self.release.ReleaseEToD()
        self.release.AddFloors()
        self.Scroll_to_documents()
        time.sleep(2)
        self.dealdetail.FinacialDocuments()
        self.elementPresenceCheck(self.text_ready_for_approval, byType='xpath')
        self.release.ReleaseDToC()

    # test_05VerifyDocumentDealInStageCtoB

    def DocumentDealInStageCtoB(self):
        time.sleep(2)
        self.Scroll_to_documents()
        time.sleep(2)
        text_to_verify = self.getText(self.text_ready_for_approval)
        original_text = "4 needed"
        self.verifyTextContains(actualText=text_to_verify, expectedText=original_text)
        time.sleep(2)
        self.dealdetail.TermSheetDocument()
        self.dealdetail.FinacialDocuments()
        self.dealdetail.DealMemo()
        self.ClickNewFinancialModel()
        self.elementPresenceCheck(self.text_ready_for_approval, byType='xpath')
        time.sleep(2)
        self.release.ClickButtonReleaseToC()
        self.release.ReleaseProcessCtoBStep2()
        self.release.ReleaseCToB()
        self.release.ReleaseMoveToB()

    # test_06VerifyDocumentDealInStageBtoA

    def DocumentDealInStageBtoA(self):
        time.sleep(2)
        self.Scroll_to_documents()
        time.sleep(2)
        text_to_verify = self.getText(self.text_ready_for_approval)
        original_text = "4 needed"
        self.verifyTextContains(actualText=text_to_verify, expectedText=original_text)
        time.sleep(2)
        self.dealdetail.TermSheetDocument()
        self.dealdetail.FinacialDocuments()
        self.dealdetail.DealMemo()
        self.ClickNewFinancialModel()
        self.LeaseUpload()
        text_to_verify_after_uploading = self.getText(self.text_ready_for_approval)
        original_text_after_uploading = "Ready for approval"
        self.verifyTextContains(actualText=text_to_verify_after_uploading, expectedText=original_text_after_uploading)
        self.elementPresenceCheck(self.text_ready_for_approval, byType='xpath')
        time.sleep(2)


    # Request changes newly uploaded required doc is on thumbnail

    '''
    Step 	
    1 Press Request changes button      
    Expected Result
    Request changes Modal appears
    
    2 Select "What needs to change" and comment and press submit
    Expected Result 
    Modal is closed and "Upload documents" cta appears
    
    3 Click "Upload documents" and change the Financial model that is present with a different financial model and press submit  
    Expected Result
    under documents, the most recent financial modal is in the thumbnail and on the thumbnail it states {"D to C release"}{Time: Just now}
        
    
    '''

    uploaded_needed = "//strong[contains(text(),'Upload needed')]"
    close_icon_to_remove_file = "//img[@class='close']"
    check_text_after_uploading_the_document = "//span[text()='D to C release']"

    # test_07VerifyRequestChangesNewlyUploadedRequiredDocIsOnThumbnail

    def RequestChangesNewlyUploadedRequiredDocIsOnThumbnail(self):
        time.sleep(2)
        self.release.ReleaseEToD()
        self.release.AddFloors()
        self.release.ReleaseDToCForm()
        time.sleep(2)
        self.request.NoApprovalButtonsAfterRequestChanges()
        time.sleep(2)
        self.elementClick(self.request.update_document)
        time.sleep(2)
        self.elementClick(self.close_icon_to_remove_file)
        time.sleep(2)
        self.release.AddFileMemoSheet()
        time.sleep(30)
        self.request.RequestModalSubmitButton()
        time.sleep(2)
        self.Scroll_to_documents()
        time.sleep(2)
        actual_text = self.getText(self.check_text_after_uploading_the_document)
        expected_text = "D to C release"
        self.verifyTextContains(actualText=actual_text, expectedText=expected_text)


    # Canceling a release request

    '''
    
    Preconditions

    User is logged into dealtrack
    User has a deal awaiting a release request approval
    User completed
    
    Steps:
    
    Click on the 'Cancel Release' CTA
    
    Expected :
    Release request is canceled and all the documents that were added for the release in the thumbnail displays: 
    {Stage canceled}{name}{Time}
    Example: {D to C release Canceled}{Rumi Begum, 2days ago} 

    
    '''

    # test_08VerifyCancelingAReleaseRequest

    click_cancel_release_request_from_overflow_menu = "//p[contains(text(),'Cancel release request')]"
    text_release_canceled = "//span[contains(text(),'(Canceled)')]"

    def CancelingAReleaseRequest(self):
        time.sleep(2)
        self.dealdetail.ClickMenuIcon()
        time.sleep(2)
        self.elementClick(self.click_cancel_release_request_from_overflow_menu)
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(2)
        self.Scroll_to_documents()
        time.sleep(2)
        actual_text = self.getText(self.text_release_canceled)
        expected_text = "Canceled"
        self.verifyTextContains(actualText=actual_text, expectedText=expected_text)






