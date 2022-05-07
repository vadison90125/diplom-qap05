from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def find_elements(self, *args):
        by, val = args[0]
        return self.driver.find_elements(by, val)

    def select(self, *args):
        by, val = args[0]
        return Select(self.driver.find_element(by, val))
