import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.release.releasing_page import ReleasePage
from selenium.webdriver.common.keys import Keys



class RequestRevisionPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.release = ReleasePage(self.driver)
        self.driver = driver


    # C53688 Request revision button says "Request changes"

    '''
    
    Preconditions

    User is logged in
    Steps

    Create or find a deal with release request when you are an approver
    Open deal details page

    Expected Result
    
    Reject button title is "Request changes"

    '''

    select_d_to_c = "//div[5]/div/div/div[2]/div[3]/div/img"
    select_c_to_b = "//div[5]/div/div/div[2]/div[5]/div/img"
    select_b_to_a = "//div[5]/div/div/div[2]/div[7]/div/img"
    request_change_button = "//span[contains(text(),'Request changes')]"

    def SelectCtoB(self):
        self.elementClick(self.select_c_to_b)

    def SelectBToA(self):
        self.elementClick(self.select_b_to_a)

    # Verify request button available on the page
    # test_01VerifyRequestRevisionButtonDToC

    def VerifyRequestRevisionButtonAvailable(self):
        time.sleep(2)
        self.release.ReleaseEToD()
        self.release.AddFloors()
        self.release.ReleaseDToCForm()
        self.VerifyRequestButton()

    def VerifyRequestButton(self):
        button_text = self.getText(self.request_change_button)
        button_text1 = "Request changes"
        self.verifyTextContains(actualText=button_text, expectedText=button_text1)


    # C53690 No approval buttons after "Request changes"

    '''
    
    Preconditions

    User is logged in
    Steps
    
    Create or find a deal with release request when you are an approver
    Open deal details page
    Click "Request changes"
    Fill in all of the fields in the modal
    Click submit
    Expected Result
    
    "Request changes" modal is dismissed
    Approval buttons ("Request changes" and "Approve release" should disappear)

    '''

    click_select_a_change_drop_down = "//select[@name='reason']"
    select_incorrect_value = "//div[@id='app']/div/div[2]/div/div/div/div/div/div/label/div/select/option[2]"
    enter_comment = "//textarea[@placeholder='Enter a comment']"
    request_modal_submit_button = "//span[contains(text(),'Submit')]"

    # Click submit button of request modal pop up
    def RequestModalSubmitButton(self):
        self.elementClick(self.request_modal_submit_button)

    # Enter comment on request modal box
    def EnterComment(self, comment):
        self.elementClick(self.enter_comment)
        time.sleep(2)
        self.sendKeys(comment, self.enter_comment)

    # GLOBAL method to add comment
    def Comment(self):
        comment = "Request release changes"
        self.EnterComment(comment)

    # click on request change button
    def ClickRequestChangeModalButton(self):
        time.sleep(2)
        self.elementClick(self.request_change_button)

    '''
    
    Steps:
    Create a new deal
    Process from e to d
    add floors
    verify request changes button
    click request change button
    select from drop down
    enter comment
    click submit
    verify upload button
    verify requested change text on approver at the bottom of the page
    scroll to upload document 
    click upload document
    click add memo and upload pdf
    Click submit
    
    '''

    doc_upload_button = "//div[@id='app']/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/button/span"
    cancel_button = "//p[contains(text(),'Cancel release request')]"
    update_document = "//span[contains(text(),'Update documents')]"

    def ClickDealDetailPageCancelButton(self):
        self.dealdetail.ClickMenuIcon()
        time.sleep(2)
        self.elementClick(self.cancel_button)
        self.dealdetail.SubmitButton()

    # test_02VerifyNoApprovalButtonsAfterRequestChanges

    def NoApprovalButtonsAfterRequestChanges(self):
        time.sleep(2)
        self.ClickRequestChangeModalButton()
        time.sleep(2)
        self.elementClick(self.select_incorrect_value)
        time.sleep(2)
        self.Comment()
        time.sleep(2)
        self.RequestModalSubmitButton()
        time.sleep(2)
        get_button = self.getText(self.update_document)
        text = "Update documents"
        self.verifyTextContains(actualText=get_button, expectedText=text)


    # CTA button should say "Upload documents"
    '''
    
    Preconditions

    User should be logged in
    Steps
    
    Find a deal that you have requested changes on
    Expected Result
    
    In the header area to the right of the approval progress bar there should be two buttons floated to the right:
    1. "Cancel release"
    2. "Upload documents"

    '''

    # test_04VerifyCTAButtonShouldSayUploadDocuments

    def CTAButtonShouldSayUploadDocuments(self):
        time.sleep(2)
        get_button = self.getText(self.update_document)
        text = "Update documents"
        self.verifyTextContains(actualText=get_button, expectedText=text)



    # C53691 Approver section updates to reflect "Requested changes" status

    '''
    
    Preconditions

    User is logged in
    Steps
    
    Create or find a deal with release request when you are an approver
    Open deal details page
    Click "Request changes"
    Fill in all of the fields in the modal
    Click submit
    Expected Result
    
    Look for your name in the Approvers section
    To the right of your name it should read in yellow text: "(Requested changes)"

    '''

    requested_changes_on_deal_detail_page = "//span[contains(text(),'Requested changes')]"
    submit_button = "//span[contains(text(),'Submit')]"

    # test_05VerifyApproverSectionUpdatesToReflectRequestedChangesStatus

    def ApproverSectionUpdatesToReflectRequestedChangesStatus(self):
        time.sleep(2)
        self.dealdetail.innerScroll(self.dealdetail.scroll_to_team)
        time.sleep(2)
        approver_request_text = self.getText(self.requested_changes_on_deal_detail_page)
        text = "Requested changes"
        self.verifyTextContains(actualText=approver_request_text, expectedText=text)

    # test_06VerifyRequestRevisionFromDToC
    def VerifyRequestRevisionFromDToC(self):
        time.sleep(2)
        # self.dealdetail.innerScrollUp(self.doc_upload_button)
        # time.sleep(2)
        self.elementClick(self.update_document)
        time.sleep(2)
        self.release.AddDealMemo()
        time.sleep(2)
        self.RequestModalSubmitButton()
        time.sleep(2)
        self.VerifyRequestButton()
        self.release.ApproveReleaseButtonClick()


    '''
    
    Click release to b button 
    Enter all the detail on the form
    Click submit on step 3
    Expected
    Verify request change button
    
    Click request change button
    Select value from drop down
    Enter comment
    Click submit
    Expected:
    Verify request button should not be shown now
    
    Scroll to the bottom of the page
    Expected:
    VERIFY Requested change text just near the approver name
    
    Scroll the screen to top
    Click on upload documenmt
    Upload the deal memo document again
    Click submit
    
    '''


    def VerifyNoApprovalButtonsAfterRequestChangesFromCtoB(self):
        self.release.ReleaseProcessCTOB()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        self.release.AddMeetingNote()
        time.sleep(2)
        self.NoApprovalButtonsAfterRequestChanges()

    def ApproverSectionUpdatesToReflectRequestedChangesStatusFromCToB(self):
        time.sleep(2)
        self.ApproverSectionUpdatesToReflectRequestedChangesStatus()

    click_first_close_icon = "//div[@id='app']/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/img"

    def VerifyRequestRevisionFromCToB(self):
        time.sleep(2)
        # self.dealdetail.innerScrollUp(self.doc_upload_button)
        # time.sleep(2)
        self.elementClick(self.doc_upload_button)
        time.sleep(2)
        self.elementClick(self.click_first_close_icon)
        time.sleep(2)
        self.release.AddDealMemo()
        time.sleep(2)
        self.RequestModalSubmitButton()
        time.sleep(2)
        self.VerifyRequestButton()


    # C53692 Deal list filter type "Needs my approval" list does not include deals where I have request changes

    '''
    
    Preconditions

    User is logged in
    Steps
    
    Find a deal that has changes requested
    Click "Update documents" (only if you are part of the deal team should you see update document)
    The submit button should be disabled.
    Click the X next to one of the file tokens to remove it
    Add a new file by clicking on the "Add file" button
    Once a new document is added, noticed the submit button is enabled
    Click submit
    Expected Result
    
    The new document should appear on the deal details page
    IF you are an approver on the deal, approval buttons should be visible again

    
    '''

    def ApprovalButtonsReturnAfterUpdatingDocumentsAfterChangesAreRequested(self):
        time.sleep(3)
        approve_button = self.getText(self.release.approve_release_button)
        approve_button_text = "Approve release"
        self.verifyTextContains(actualText=approve_button, expectedText=approve_button_text)
        time.sleep(3)
        self.release.ApproveReleaseButtonClick()


    '''
    
    Click button release to a
    Ente all the details and click submit
    Expected:
    Verify request button should be there
    
    Click requested buttoon
    Enter comment and select value from drop down
    Click submit
    Scroll to bottom of screen
    Expected:
    Verify approver text at the bottom of the screen. 
    
    Scroll to the top and click on upload document
    Upload deal memo doc
    Click submit
    
    '''

    def VerifyNoApprovalButtonsAfterRequestChangesFromBtoA(self):
        self.release.ReleaseMoveToB()
        self.release.ReleasePopUpFieldEntry()
        time.sleep(2)
        self.dealdetail.SubmitButton()
        time.sleep(2)
        self.NoApprovalButtonsAfterRequestChanges()

    def ApproverSectionUpdatesToReflectRequestedChangesStatusFromBToA(self):
        time.sleep(2)
        self.ApproverSectionUpdatesToReflectRequestedChangesStatus()

    click_first_close_from_b_to_c = "//div[@id='app']/div/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/img"

    def VerifyRequestRevisionFromBToA(self):
        time.sleep(2)
        # self.dealdetail.innerScrollUp(self.doc_upload_button)
        # time.sleep(2)
        self.elementClick(self.doc_upload_button)
        time.sleep(2)
        self.elementClick(self.click_first_close_icon)
        time.sleep(2)
        self.release.AddDealMemo()
        time.sleep(2)
        self.RequestModalSubmitButton()
        time.sleep(2)
        self.VerifyRequestButton()
        self.release.ApproveReleaseButtonClick()


    # C53692 Deal list filter type "Needs my approval" list does not include deals where I have request changes

    '''
    
    Preconditions

    User has logged in
    Steps

    Create or find deal that needs your approval
    Navigate to deal from “Needs my approval”
    Click "Request changes"
    Navigate back to “Needs my approval”

    Expected Result
    
    The deal should not appear in the "Needs my approval" deal list
    
    '''


    # change deal name
    deal_name_change = "//input[@placeholder='Unknown']"

    def ChangeDealName(self, dealname):
        time.sleep(2)
        self.elementClick(self.deal_name_change)
        time.sleep(2)
        self.clearField(self.deal_name_change)
        self.sendKeys(dealname, self.deal_name_change)

    # Enter deal name
    def EnterDealName(self):
        time.sleep(2)
        dealname = "001 Udaipur"
        self.ChangeDealName(dealname)

    more_filter = ".sidebar--header-icon:nth-child(4)"
    search_textbox = "//input[@placeholder='Search for deals']"
    no_deal_found = "//h3[contains(text(),'No deals matching your filters')]"

    def EnterSearchTextBox(self, name):
        self.elementClick(self.search_textbox)
        time.sleep(2)
        self.sendKeys(name, self.search_textbox)

    def PressEnter(self, value):
        self.sendKeys(value, self.search_textbox)

    def DealRemovedFromNeedMyApprovalAfterRequestChanges(self):
        time.sleep(2)
        self.elementClick(self.deal.more_filter_icon)
        time.sleep(2)
        self.deal.ClickStageField()
        time.sleep(2)
        self.SelectCtoB()
        time.sleep(2)
        self.deal.ClickApplyButton()
        time.sleep(2)
        self.EnterDealName()
        time.sleep(2)
        self.NoApprovalButtonsAfterRequestChanges()
        time.sleep(2)
        # self.deal.ClickBackArrow()
        # time.sleep(4)
        name = "001 Udaipur"
        self.EnterSearchTextBox(name)
        time.sleep(2)
        self.PressEnter(Keys.ENTER)
        time.sleep(2)
        no_deal_text = self.getText(self.no_deal_found)
        deal_text = "No deals matching your filters"
        self.verifyTextContains(actualText=no_deal_text, expectedText=deal_text)
























        














