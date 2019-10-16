import time
import datetime
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages
from deal_pages.unrelease.unrelease_pages import UnReleasePages
from deal_pages.release.releasing_page import ReleasePage


class KeyChangesPages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.unrelease = UnReleasePages(self.driver)
        self.release = ReleasePage(self.driver)
        self.driver = driver

    # Key changes chart does not show on deals with no previous data

    '''
    
    Preconditions

    User is logged in to dealtrack
    
    Steps

    Click on the (+) on the bottom left of the page to add a new deal
    Enter a new address
    Click Add
    Go to the deal details page of deal added

     Expected Result

    Above the “Ganeral Info” & below Timeline section of the deal details page, there should be no mention of “Key changes”
    
    Note : This section will be displayed once deal is released to stage D & floors been added

    
    '''

    scroll_to_financial = "//a[contains(text(),'Financials')]"
    key_changes_text = "//span[contains(text(),'Key changes since release')]"

    def ClickFinancialTab(self):
        self.elementClick(self.scroll_to_financial)

    def VerifyKeyChangesChartDoesNotShowOnDealsWithNoPreviousData(self):
        time.sleep(2)
        self.deal.AddNewDeal()
        time.sleep(2)
        self.ClickFinancialTab()
        time.sleep(2)
        if not self.isElementDisplayed(self.key_changes_text):
            self.log.info('Pass')
            assert True
        else:
            self.log.info('Fail')
            assert False

    # Key changes chart only shows values that have changed

    '''
    
    Preconditions

    User is logged in to dealtrack
    User created a deal in E:(https://wework.testrail.net/index.php?/cases/view/58647&group_by=cases:section_id&group_id=6586&group_order=asc )
    
    Steps

    Navigate to the deal created
    Click 'Release to D' CTA button
    In Modal add a Real estate manager
    Enter Desks and RSF values and select Est. C release and Possession date (remember RSF and Desk values)

    Press submit
    Observe: note there is no Key changes section!

    Click 'Add floors' CTA
    in 'Add floors' text box add '1' and press enter on keyboard
    In RSF add a different value than previously added in release to D modal, add USF value, add a different Desks value than previously added in release to D modal
    Add Possession and Opening dates
    Press save
    
    
    Expected Result
    
    On deal details page under description there is a Key changes since release section with a drop down stating the most recent stage (Stage D (Sourcing)) (this example will not have any other options in dropdown)

    Within chart you will see 4 columns: Data point column (Desks, RSF), Stage 'D ' (will change depending on stage, column contains the original value in that particular stage), Now (the changed value), Change (if it has Increased with a upward arrow icon in front, Decreased with a downward arrow in front, Added or Removed)

    Key Changes will have data points
    Desk
    RSF


    '''

    desk_text = "//strong[contains(text(),'Desks')]"
    rsf_text = "//strong[contains(text(),'RSF')]"
    now_text = "//p[contains(text(),'Now')]"
    change_text = "//p[contains(text(),'Change')]"

    def VerifyKeyChangesChartOnlyShowsValuesThatHaveChanged(self):
        time.sleep(2)
        self.release.ReleaseEToD()
        self.release.AddFloors()
        self.isElementDisplayed(self.key_changes_text)
        self.isElementPresent(self.desk_text)
        self.isElementPresent(self.rsf_text)
        self.isElementPresent(self.now_text)
        self.isElementPresent(self.change_text)

    increase_decrease_change = ".sc-1c6ibka-0:nth-child(2) > .key-changes--change-column > .Mono-sc-1pt1tnu"

    def CheckChangeInText(self):
        self.getText(self.increase_decrease_change, locatorType='css')

    def VerifyChangeColumnVariation(self):
        time.sleep(2)
        actual_text = self.getText(self.increase_decrease_change, locatorType='css')
        expected_text = "Decreased"
        self.verifyTextContains(actualText=actual_text, expectedText=expected_text)

    # Change column signifies change in data D-C

    '''
    
    Preconditions

    User is logged in to Dealtrack
    Page must be viewed with browser in full screen
    User has created a deal that has Key changes section: in Stage D (https://wework.testrail.net/index.php?/cases/view/58648&group_by=cases:section_id&group_id=6586&group_order=asc )
    
    Steps:
    Click Release to C
    
	Expected
    Release to C modal appears
    
    2 Upload Financial Model
      Update required deal info and add approvers
      Press submit
        
    Expected
    Release is submitted and modal is closed, once FiMo is done scrapping observe 'Key changes since release' has data points:
    -RSF
    -USF/desk
    -Gross construction cost
    -EBITDA
    -Payback
    -IRR
    
    3 Observe 'Stage D' column has '-' and 'Now' column has the value scrapped from Financial Model
        
    Expected
    'Now' column should display scraped values from Financial Model for data points with any changes:
    -Rent
    -Desks
    -RSF
    -USF/desk
    -Gross construction cost
    -EBITDA
    -Payback
    -IRR
    
    
    4 The column on the far right of the key changes chart should be labeled “Change”
        
    Expected
    Change with display if the change has increased, decreased, added or removed

 
    '''

    usf_desk = "//strong[contains(text(),'USF/desk')]"
    gross_construction_cost = "//strong[contains(text(),'Gross construction cost')]"
    ebitda = "//strong[contains(text(),'EBITDA')]"
    payback = "//strong[contains(text(),'Payback')]"
    irr = "//strong[contains(text(),'IRR')]"

    def VerifyDataChangeAfterReleasingDtoC(self):
        self.release.ReleaseDToCForm()
        time.sleep(2)
        self.ClickFinancialTab()
        time.sleep(2)
        self.isElementPresent(self.usf_desk)
        self.isElementPresent(self.gross_construction_cost)
        self.isElementPresent(self.ebitda)
        self.isElementPresent(self.payback)
        self.isElementPresent(self.irr)

    change_value = "//div[@id='financials']//div[2]/div[2]/div[1]"

    def VerifyChangesInChangeColumn(self):
        time.sleep(2)
        actual_text = self.getText(self.increase_decrease_change, locatorType='css')
        expected_text = "added"
        self.verifyTextContains(actualText=actual_text, expectedText=expected_text)

    def ChangeColumnSignifiesChangeInDataCToB(self):
        time.sleep(2)
        self.release.ReleaseProcessCTOB()

