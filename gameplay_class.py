import time
from multiprocessing import Process
from selenium.webdriver.common.by import By


class GamePlay:

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        self.find = selenium_driver.find_element
        # self.golden_cookie = '# // *[ @ id = "shimmers"] / div'

    @property
    def cookies(self):
        cookies = self.find(by=By.XPATH, value='//*[@id="cookies"]').get_attribute('innerHTML')
        cookies_no = cookies.split(' ')[0]
        return int(cookies_no)

    @property
    def in_game_cps(self):
        cookies_raw = self.find(by=By.XPATH, value='//*[@id="cookies"]').get_attribute('innerHTML')
        cps = cookies_raw.split('per second: ')[1][0:-6]
        return cps

    def cookies_per_second(self):
        cookies_1 = self.cookies
        time.sleep(1)
        cookies_2 = self.cookies
        total_cps = cookies_2 - cookies_1

    def click_cookie(self):
        for x in range(5):
            self.find(by=By.XPATH, value='//*[@id="bigCookie"]').click()

    def gameplay(self):
        self.in_game_cps


