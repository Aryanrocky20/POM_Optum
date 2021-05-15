from selenium.webdriver.common.by import By
from Utilities.readConfiguraion import ReadProperties


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username = ReadProperties.readLocators("LocatorsData", "textbox_username_id")
        self.password = ReadProperties.readLocators('LocatorsData', 'textbox_password_id')
        self.login = ReadProperties.readLocators('LocatorsData', 'button_login_id')
        self.forgot = ReadProperties.readLocators('LocatorsData', 'link_forgot_xpath')
        self.logout = ReadProperties.readLocators('LocatorsData', 'link_logout_xpath')

    def enterUserName(self, email):
        print(self.username)
        self.driver.find_element(By.ID, self.username).clear()
        self.driver.find_element(By.ID, self.username).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, self.password).clear()
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.login).click()

    def clickForgotPassword(self):
        self.driver.find_element(By.XPATH, self.forgot).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout).click()
