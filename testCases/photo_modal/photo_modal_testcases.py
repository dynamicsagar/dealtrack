from deal_pages.photo_modal.photo_modal import PhotoModalPages
import utilities.custom_logger as cl
import unittest
import pytest
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PhotoModalTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.photo = PhotoModalPages(self.driver)

    def test_01VerifyButtonToUploadNewPhoto(self):
        self.log.info("*#" * 20)
        self.log.info(" test_01VerifyButtonToUploadNewPhoto ")
        self.log.info("*#" * 20)
        self.photo.VerifyButtonToUploadNewPhoto()

    def test_02VerifyUploadPhotoReplaceDefaultPhoto(self):
        self.log.info("*#" * 20)
        self.log.info(" test_02VerifyUploadPhotoReplaceDefaultPhoto ")
        self.log.info("*#" * 20)
        self.photo.VerifyUploadPhotoReplaceDefaultPhoto()

    def test_03VerifyClickingOnAPhotoLaunchesPhotoGridModal(self):
        self.log.info("*#" * 20)
        self.log.info(" test_03VerifyClickingOnAPhotoLaunchesPhotoGridModal ")
        self.log.info("*#" * 20)
        self.photo.ClickingOnAPhotoLaunchesPhotoGridModal()

    def test_04VerifyUserCanUploadUntaggedPhoto(self):
        self.log.info("*#" * 20)
        self.log.info(" test_04VerifyUserCanUploadUntaggedPhoto ")
        self.log.info("*#" * 20)
        self.photo.UserCanUploadUntaggedPhoto()

    def test_05VerifyUntaggedPhotoSlotKeepsCountOfAllUntaggedPhotos(self):
        self.log.info("*#" * 20)
        self.log.info(" test_05VerifyUntaggedPhotoSlotKeepsCountOfAllUntaggedPhotos ")
        self.log.info("*#" * 20)
        self.photo.UntaggedPhotoSlotKeepsCountOfAllUntaggedPhotos()

    def test_06VerifyByAddingEditingTag(self):
        self.log.info("*#" * 20)
        self.log.info(" test_06VerifyByAddingEditingTag ")
        self.log.info("*#" * 20)
        self.photo.EditTag()

    def test_07VerifyByUploadingPhotoToSignage(self):
        self.log.info("*#" * 20)
        self.log.info(" test_07VerifyByUploadingPhotoToSignage")
        self.log.info("*#" * 20)
        self.photo.ClickUploadSignageToAddPhoto()

    def test_08VerifyByRemovingTheTag(self):
        self.log.info("*#" * 20)
        self.log.info(" test_08VerifyByRemovingTheTag- Check default count ")
        self.log.info("*#" * 20)
        self.photo.RemoveTag()

    def test_09VerifyByDeletingTheTag(self):
        self.log.info("*#" * 20)
        self.log.info(" test_09VerifyByDeletingTheTag- Check default new image icon on popup ")
        self.log.info("*#" * 20)
        self.photo.DeletePhoto()


