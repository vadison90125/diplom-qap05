from page.base_page import BasePage
from selenium.webdriver.common.by import By


seller_name = (By.XPATH, '//h1[contains(.,"4AVTO.by")]')


class SellerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def seller_name(self):
        if '4AVTO.by' in self.find_element(seller_name).text:
            seller = '4AVTO.by'
        else:
            seller = 'Не 4AVTO.by'
        return seller
