from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


num_ad = (By.CLASS_NAME, 'badge')
delete = (By.XPATH, '//i[@class="fa fa-trash-o fa-lg"]')
text_ad = (By.XPATH, '//b[text()="Эмблема"]')


class ListAdPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def num_ad(self):
        return self.find_elements(num_ad)[1].text

    def delete_ad_click(self):
        self.find_element(delete).click()

    def text_ad(self):
        try:
            self.find_element(text_ad).is_displayed()
        except (StaleElementReferenceException, NoSuchElementException):
            return True
        return False
