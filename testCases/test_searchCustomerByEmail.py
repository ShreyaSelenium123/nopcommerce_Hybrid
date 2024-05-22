import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("***** SearchCustomerByEmail_004 ****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login succesful ****")

        self.logger.info("*** Starting Search Customer By Email ****")

        self.addcust = AddCustomer(self.driver)
        time.sleep(5)
        self.addcust.clickOnCustomersMenu()
        time.sleep(5)
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(5)

        self.logger.info("***** searching customer by emailID ****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        time.sleep(2)
        searchcust.clickSearch()
        time.sleep(2)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("*****  TC_SearchCustomerByEmail_004 Finished  ***** ")