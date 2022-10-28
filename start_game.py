import time
from helpers import element_by_xpath
from selenium.common.exceptions import StaleElementReferenceException


def start_game(selenium_driver):

    COOKIE_CLICKER_URL = "https://orteil.dashnet.org/cookieclicker/"

    selenium_driver.get(COOKIE_CLICKER_URL)

    element_by_xpath('//*[@id="langSelect-EN"]', selenium_driver).click()
    element_by_xpath('/html/body/div[1]/div/a[1]', selenium_driver).click()

    while True:
        try:
            element_by_xpath('//*[@id="notes"]/div[3]', selenium_driver).click()
        except StaleElementReferenceException:
            time.sleep(1)
        else:
            break


