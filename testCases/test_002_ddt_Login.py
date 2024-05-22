import time

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import UTlityxl

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path=".\\testData\\LoginTest.xlsx"
    logger = LogGen.loggen()


    def test_login_ddt(self,setup):
        self.logger.info("***Starting Test_002_DDT_Login*****")
        self.logger.info("***Starting Login DD Test*****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)

        self.rows=UTlityxl.getRowCount(self.path,"Sheet1")
        print("Number of row ",self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=UTlityxl.readData(self.path,"Sheet1",r,1)
            self.password=UTlityxl.readData(self.path,"Sheet1",r,2)
            self.exp=UTlityxl.readData(self.path,"Sheet1",r,3)
            self.lp.setUsername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("pass")
            elif act_title != exp_title:
                if self.exp=="pass":
                    self.logger.info("** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("fail")
                elif self.exp=="fail":
                    self.logger.info("** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("pass")
        if "fail" not in lst_status:
            self.logger.info("**DDT Login test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("**DDT Login test Faild ***")
            self.driver.close()
            assert False
        self.logger.info("**End Login DDT Test ***")
        self.logger.info("**Complete Tc_002_loginDDT***")










