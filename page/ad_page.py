from page.base_page import BasePage
from selenium.webdriver.common.by import By


seller = (By.LINK_TEXT, '4AVTO.BY')
add_to_note = (By.CSS_SELECTOR, 'a[class="favorite"]')


class AdPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def seller_click(self):
        self.find_element(seller).click()

    def add_to_note_click(self):
        self.find_element(add_to_note).click()
