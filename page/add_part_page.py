from page.base_page import BasePage
from selenium.webdriver.common.by import By


add_ad_button = (By.XPATH, '//a[@class="btn btn-success btn-sm abtn"]')
my_ad = (By.XPATH, '//a[text()=" Показать мои з/ч"]')


class AddPartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_ad_button_click(self):
        self.find_elements(add_ad_button)[0].click()

    def my_ad_click(self):
        self.find_element(my_ad).click()
