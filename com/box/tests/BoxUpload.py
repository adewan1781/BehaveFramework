from com.box.steps.BoxLoginSteps import BoxLoginSteps
from com.box.steps.BoxUploadSteps import BoxUploadSteps

if __name__ == '__main__':
    obj = BoxLoginSteps()
    obj.verifyPageTitle("Box | Login")
    obj.loginProcess("nancydhingra131@gmail.com", "nancy131")
    obj.verifyPageTitle("All Files | Powered By Box")
    obj1 = BoxUploadSteps()
    obj1.selectFolderToGoIn()
    obj.verifyPageTitle ("serious123 | Powered By Box")
    obj1.clickUploadMenu()
    obj1.uploadFile("/Users/rk/Documents/Zscaler.png")
    obj1.verifyUpload()
    obj1.selectRowToDelete()
    obj1.deleteRow()
    obj.logOutProcess ()
    obj.verifyPageTitle ("Box | Login")


