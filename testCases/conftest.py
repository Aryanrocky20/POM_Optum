from csv import excel

import pytest
from selenium import webdriver
import os
from Utilities.readConfiguraion import ReadProperties

@pytest.fixture()
def setup():
    base_url = ReadProperties.readConfiguration("configuration", "base_url")
    username = ReadProperties.readConfiguration("configuration", "username")
    password = ReadProperties.readConfiguration("configuration", "password")
    browser = ReadProperties.readConfiguration("configuration", "browser")

    if browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=".\driver\chromedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path=".\driver\chromedriver.exe")

    driver.maximize_window()
    driver.get(base_url)
    return driver




########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Optum'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Yash'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)