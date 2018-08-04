from com.box.steps.BoxLoginSteps import BoxLoginSteps

if __name__ == '__main__':
    obj = BoxLoginSteps()
    obj.verifyPageTitle("Box | Login")
    obj.loginProcess("nancydhingra131@gmail.com", "nancy131")
    obj.verifyPageTitle("All Files | Powered By Box")
    obj.logOutProcess()
    obj.verifyPageTitle("Box | Login")
    obj.driverQuit()