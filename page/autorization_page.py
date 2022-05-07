from page.base_page import BasePage
from selenium.webdriver.common.by import By


login = (By.CSS_SELECTOR, 'input[name="USER_LOGIN"]')
password = (By.CSS_SELECTOR, 'input[name="USER_PASSWORD"]')
button_login = (By.CSS_SELECTOR, 'input[value="Войти"]')


class AutorizationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        self.find_element(login).send_keys('ilmor2000@mail.ru')

    def password(self):
        self.find_element(password).send_keys('protuberans2000')

    def button_login_click(self):
        self.find_element(button_login).click()
