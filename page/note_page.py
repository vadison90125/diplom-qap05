from page.base_page import BasePage
from selenium.webdriver.common.by import By


ad_in_note = (By.XPATH, '//a[text()="Барабан тормозной к Богдан А092, 2003 г. "]')
button_clear_note = (By.CLASS_NAME, 'js-clear-favorite-btn')
text = (By.XPATH, '//b[contains(.,"Нет объявлений в блокноте")]')


class NotePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def ad_in_note(self):
        return self.find_element(ad_in_note).text

    def button_clear_note_click(self):
        self.find_element(button_clear_note).click()

    def note_text(self):
        return self.find_element(text).text
