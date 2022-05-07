from page.base_page import BasePage
from selenium.webdriver.common.by import By


input_item = (By.CLASS_NAME, 'select2-search__field')
mark = (By.ID, 'SELECT_MARKA_ID')
model = (By.ID, 'SELECT_MODEL_ID')
year = (By.ID, 'year')
part = (By.XPATH, '//select[@name="TAG_ID"]')
cost = (By.XPATH, '//input[@name="PRICE"]')
flag = (By.XPATH, '//input[@class="lk-radio-currency"]')
activation = (By.XPATH, '//input[@type="checkbox"]')
save_ad = (By.XPATH, '//button[@type="submit"]')
all_ad = (By.CLASS_NAME, 'btn-xs')


class NewPartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def mark_select(self):
        self.select(mark).select_by_value('9688')

    def model_select(self):
        self.select(model).select_by_value('9721')

    def year_input(self):
        self.find_element(year).send_keys('2022')

    def part_select(self):
        self.select(part).select_by_value('1813')

    def flag_click(self):
        self.find_elements(flag)[0].click()

    def cost_input(self):
        self.find_element(cost).send_keys('100')

    def activation_click(self):
        self.find_element(activation).click()

    def save_ad_click(self):
        self.find_element(save_ad).click()

    def all_ad_click(self):
        self.find_element(all_ad).click()
