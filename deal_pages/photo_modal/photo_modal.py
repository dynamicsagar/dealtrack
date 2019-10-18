import time
from base.selenium_driver import SeleniumDriver
from deal_pages.deal_list_screen.deal_list_screen_page import DealList
from deal_pages.deals_detail_screen.deals_detail_screen_pages import DealDetailScreenPages


class PhotoModalPages(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.deal = DealList(self.driver)
        self.dealdetail = DealDetailScreenPages(self.driver)
        self.driver = driver


    # Deal details > Photo Modal

    """
    1.Navigate to deal with no uploaded photos
    
    Expected :
    Button to upload “New photo” should be over google street view photo greyed out
    
    """

    default_photo = "//span[contains(text(),'New photo')]"

    def VerifyButtonToUploadNewPhoto(self):
        time.sleep(2)
        self.deal.AddNewDeal()
        time.sleep(2)
        text = "New photo"
        text_photo = self.getText(self.default_photo)
        time.sleep(2)
        self.verifyTextContains(actualText=text, expectedText=text_photo)


    # TC -02 "Uploading “main” photo replaces Google street view photo"

    """
    
    Steps:
    1.Navigate to deal with no uploaded photos
    2.Hover over the default google street view photo
    3.Click on the prompt to add “New photo”
    4.Upload photo
    
    Expected :
    The uploaded photo should replace the google street view photo in the grid
    
    """

    def VerifyUploadPhotoReplaceDefaultPhoto(self):
        time.sleep(2)
        self.dealdetail.AddPhotos()


    # TC-03 Clicking on a photo launches photo grid modal

    """
    
    "Clicking on a photo launches photo grid modal"
    1.Navigate to deal with at least one uploaded photo
    2.Click on uploaded photo in the photo grid
    
    Expected :
    1.Photo viewing modal should be launched and should see all targets with upload link next to target name
    
    """

    def ClickingOnAPhotoLaunchesPhotoGridModal(self):
        time.sleep(2)
        self.dealdetail.VerifyPhotoAddedSuccessfully()


    # TC-04 "User can upload untagged photo"

    """
    
    "User can upload untagged photo"
    1.Navigate to deal with no uploaded photos
    2.Click on photo grid slot that does NOT have a photo tag label
    3.Upload a photo
    
    Expected :
    The preview for that slot in the photo grid should be replaced with a preview of the uploaded photo
    
    """

    untagged_photo = ".sc-108qnys-0:nth-child(1)" # change might be needed

    def UserCanUploadUntaggedPhoto(self):
        time.sleep(2)
        self.elementClick(self.untagged_photo, locatorType='css')
        time.sleep(2)
        name = "C:/Users/Sagar/Desktop/360degreeimages/R0010005.JPG"
        self.dealdetail.UploadDocuments(name)
        time.sleep(4)
        self.dealdetail.ClickUploadButton()
        time.sleep(25)
        self.dealdetail.VerifyPhotoAddedSuccessfully()


    # TC-05 "Untagged photo slot keeps count of all untagged photos "

    """
    
    "Untagged photo slot keeps count of all untagged photos "
    1.Navigate to deal with no uploaded photos
    2.Click on photo grid slot that does NOT have a photo tag label
    3.Upload four photos
    
    Expected:
    There should be a count at the top of that photo grid slot that says “+3 more”
    
    """

    other_photos_upload_link = "//div[7]//div[1]//div[1]//strong[1]"
    count_untagged_photo = "//div[contains(text(),'+ 3 more')]"
    click_other_photo_after_upload = ".tag:nth-child(6) > img"

    def UntaggedPhotoSlotKeepsCountOfAllUntaggedPhotos(self):
        time.sleep(4)
        self.dealdetail.ClickUploadedImage()
        time.sleep(2)
        self.innerScroll(self.other_photos_upload_link)
        time.sleep(2)
        for i in range(0, 3):
            self.elementClick(self.other_photos_upload_link)
            time.sleep(2)
            name = "C:/Users/Sagar/Desktop/360degreeimages/R0010005.JPG"
            self.dealdetail.UploadDocuments(name)
            time.sleep(4)
            self.dealdetail.ClickUploadButton()
            time.sleep(25)

        self.dealdetail.ClickPhotoModalCloseIcon()
        time.sleep(2)
        text = "+ 3 more"
        text_untagged_photo = self.getText(self.count_untagged_photo)
        self.verifyTextContains(actualText=text, expectedText=text_untagged_photo)


    # TC-06 Deal details > Adding/editing photo tags

    """
    Preconditions

    User should be on deal details screen
    Images should be attached

    Steps:
    "Order of the tags on photos from deal details page"
    1.Click on any deal from the dealist screen
    2.Add photos if not added
    3.Click on "..." icon from any uploaded photo
    4.Click on Add tag option
    5.Select any of the tag
    6.Repeat steps 3-5 on remaining photos
    7.Click on Save button

    Expected:
    Order of tagged photos should be :
    - Main
    - Streetscape
    - Signage
    - Interior
    - Exterior
    - Lobby
        
    """

    photo_menu_icon = ".photo-tour--tag-group:nth-child(1) .sc-1dok22n-0"
    edit_photo_tag = "//strong[contains(text(),'Edit photo tag')]"
    streetscape = "//p[contains(text(),'Streetscape')]"
    save_button = "//button[contains(text(),'Save')]"

    def ClickPhotoMenuIcon(self):
        self.elementClick(self.photo_menu_icon, locatorType='css')

    def EditTag(self):
        time.sleep(2)
        self.dealdetail.ClickUploadedImage()
        time.sleep(2)
        self.ClickPhotoMenuIcon()
        time.sleep(2)
        self.elementClick(self.edit_photo_tag)
        time.sleep(2)
        self.elementClick(self.streetscape)
        time.sleep(2)
        self.elementClick(self.save_button)

    signage_upload_link = ".photo-tour--tag-group:nth-child(3) .Strong-sc-jrot7n"
    click_uploaded_image = "//div[@id='app']/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div/div/img"
    zoom_button = "(//button[@type='button'])[3]"
    close_icon = ".ril-close"


    def ClickUploadSignageToAddPhoto(self):
        time.sleep(4)
        self.elementClick(self.signage_upload_link, locatorType='css')
        time.sleep(3)
        name = "C:/Users/Sagar/Desktop/360degreeimages/R0010005.JPG"
        self.dealdetail.UploadDocuments(name)
        time.sleep(4)
        self.dealdetail.ClickUploadButton()
        time.sleep(25)
        self.elementClick(self.click_uploaded_image)
        self.elementPresenceCheck(self.zoom_button, byType='xpath')
        time.sleep(2)
        self.elementClick(self.close_icon, locatorType='css')


    click_upload_new_photo_main_section = "//div[@id='app']/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/span/span"
    remove_tag = "//button[contains(text(),'Remove tag')]"
    count_untagged_photo_after_update = "//div[contains(text(),'+ 4 more')]"

    def RemoveTag(self):
        time.sleep(2)
        self.elementClick(self.click_upload_new_photo_main_section)
        time.sleep(2)
        name = "C:/Users/Sagar/Desktop/360degreeimages/R0010005.JPG"
        self.dealdetail.UploadDocuments(name)
        time.sleep(4)
        self.dealdetail.ClickUploadButton()
        time.sleep(20)
        self.ClickPhotoMenuIcon()
        time.sleep(2)
        self.elementClick(self.edit_photo_tag)
        time.sleep(2)
        self.elementClick(self.remove_tag)
        time.sleep(2)
        self.dealdetail.ClickPhotoModalCloseIcon()
        time.sleep(2)
        text = "+ 4 more"
        text_untagged_photo = self.getText(self.count_untagged_photo_after_update)
        self.verifyTextContains(actualText=text, expectedText=text_untagged_photo)

    delete_photo_link = "//strong[contains(text(),'Delete photo')]"
    delete_button = "//button[contains(text(),'Delete photo')]"


    def DeletePhoto(self):
        time.sleep(2)
        self.VerifyUploadPhotoReplaceDefaultPhoto()
        time.sleep(2)
        self.dealdetail.ClickUploadedImage()
        time.sleep(2)
        self.ClickPhotoMenuIcon()
        time.sleep(2)
        self.elementClick(self.delete_photo_link)
        time.sleep(4)
        self.elementClick(self.delete_button)
        time.sleep(4)
        self.elementPresenceCheck(self.click_upload_new_photo_main_section, byType='xpath')
















