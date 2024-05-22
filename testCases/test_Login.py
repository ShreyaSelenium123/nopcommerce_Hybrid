from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    baseURL =ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()

    logger =LogGen.loggen()
    def test_homePageTitle(self,setup):
        self.logger.info("************Test_001_log***************")
        self.logger.info("************Verifying Home Page***************")

        self.driver=setup
        self.driver.get(self.baseURL)
        acc_title=self.driver.title
        #self.driver.close()
        if acc_title=="Your store. Login":
            assert True
            self.logger.info("*****************Home Page title test is Passed*******************")
        else:
            self.driver.save_screenshot(r".\\Screenshots\\homepage.png")
            self.driver.close()

            assert False


    def test_login(self,setup):
        self.logger.info("*****************To Verify Login page *******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        ac_title=self.driver.title
        #self.driver.close()
        if ac_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****************Login Page test is Passed*******************")

            self.driver.save_screenshot(r".\\Screenshots\\loginpass.png")

        else:
            assert False

