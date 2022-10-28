import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def element_by_xpath(path, selenium_driver):
    while True:
        try:
            selenium_driver.find_element(by=By.XPATH, value=path)

        except (NoSuchElementException, AttributeError) as e:
            print('Element not found yet')
            time.sleep(1)

        else:
            return selenium_driver.find_element(by=By.XPATH, value=path)
