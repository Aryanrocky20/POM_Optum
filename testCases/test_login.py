import pytest
from pageObjects.LoginPage import LoginPage
from Utilities import XLUtilities
from selenium import webdriver
from Utilities.customLogger import LogGen
import time

class Test_001_Login:
    username = "ykumar@myhealthdirect.com"
    password = "Abcd@123"

    logger = LogGen.loggen()

    def test_incorrectLogin(self, setup):
        self.logger.info("************** Test_001_Login **************")
        self.logger.info("************** Incorrect Login **************")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)

        act_title = self.driver.title
        if act_title == "System List - MyHealthDirect":
            self.logger.info("************** Login Successful **************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_incorrectLogin.png")
            self.logger.info("************** Login Failed **************")
            assert False
            self.driver.close()
