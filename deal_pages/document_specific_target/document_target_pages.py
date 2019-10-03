import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages


class DocumentSpecificPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deall = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
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

    scroll_to_documents = "//span[contains(text(),'Documents')]"
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
        self.getElement(self.scroll_to_documents)

    def VerifyDocumentView(self):
        time.sleep(2)
        self.deall.AddNewDeal()
        time.sleep(2)
        self.innerScroll(self.Scroll_to_documents())
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

    click_lease_upload_pdf = ".sc-12w36a0-0:nth-child(4) svg"
    click_budget_upload_xls = ".sc-12w36a0-0:nth-child(5) svg"
    click_ops_rider_upload_pdf = ".sc-12w36a0-0:nth-child(6) svg"
    click_programing_pkg_upload_pdf = ".sc-12w36a0-0:nth-child(7) svg"
    click_project_schedule_upload_pdf = ".sc-12w36a0-0:nth-child(8) svg"
    click_revOps_upload_xls = ".sc-12w36a0-0:nth-child(9) svg"
    click_test_fit_upload_pdf = ".sc-12w36a0-0:nth-child(10) svg"
    click_other_attachment_upload_pdf = ".sc-12w36a0-0:nth-child(11) svg"


    def UploadPDF(self):
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/1.pdf"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(15)

    def UploadCSV(self):
        doc = "C:/Users/Sagar/PycharmProjects/DealTrack/files/FiMo.xlsm"
        self.dealdetail.UploadDocuments(doc)
        time.sleep(20)

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

    lock_icon = ".Regular-sc-ju30to svg"

    def LockIcon(self):
        self.getElement(self.lock_icon, locatorType='css')

    def VerifyLockIconAfterUploadingLeaseDocument(self):
        time.sleep(2)
        self.isElementPresent(self.LockIcon())














