import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages


class TargetZonePages(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.deall = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.driver = driver

    select_item_list = "//li[@id='search-bar-item-0']/div/p[2]"
    market_tier_flag = "//li[2]//span[2]"

    click_financial = "//a[contains(text(),'Financials')]"

    def DealDetailPageShowsWhetherADealFallsWithinTargetZone(self):
        time.sleep(2)
        self.elementClick(self.deall.click_arrow_img)
        time.sleep(2)
        self.elementClick(self.deall.click_add_new_deal)
        time.sleep(2)
        deal_name = "231 Hudson Street"
        self.deall.EnterDeal(deal_name)
        time.sleep(3)
        self.elementClick(self.select_item_list)
        time.sleep(2)
        self.elementClick(self.deall.click_add_button)
        time.sleep(5)
        self.elementClick(self.click_financial)
        time.sleep(2)
        text = self.getText(self.market_tier_flag)
        time.sleep(2)
        if text == 'Flagship':
            actual_text = "Flagship"
            self.verifyTextContains(actualText=text, expectedText=actual_text)
        elif text == 'Growth':
            actual_text = "Growth"
            self.verifyTextContains(actualText=text, expectedText=actual_text)
        else:
            self.log.info("No deal flag found")
            assert False

    icon = ".sc-1h4l0u6-0 path"
    target_zone_text = "//span[contains(text(),'Deal within Target Zone')]"

    click_location_tab = "//a[contains(text(),'Location')]"

    def VerifyTargetZoneIcon(self):
        time.sleep(2)
        self.elementClick(self.click_location_tab)
        time.sleep(2)
        self.log.info('Scroll')
        self.isElementPresent(self.icon, locatorType='css')

    def VerifyTargetZoneText(self):
        time.sleep(2)
        text = 'Deal within Target Zone'
        text1 = self.getText(self.target_zone_text)
        self.verifyTextContains(actualText=text, expectedText=text1)

