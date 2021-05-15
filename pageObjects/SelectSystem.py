from selenium.webdriver.common.by import By
from Utilities import readConfiguraion


class SelectSystem:

    def __init__(self, driver):
        driver = driver
        self.select_alphabet = readConfiguraion.readLocators('locators', 'link_y_system_xpath')
        self.select_system = readConfiguraion.readLocators('locators', 'link_system_link_text')

    def selectSystem(self):
        self.driver.find_elements(By.XPATH, self.select_alphabet).click()
        self.driver.find_elements(By.LINK_TEXT, self.select_system)
