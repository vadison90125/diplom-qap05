from page.base_page import BasePage
from selenium.webdriver.common.by import By


button_enter = (By.LINK_TEXT, 'ВХОД')
button_next = (By.CLASS_NAME, 'modern-page-next')
number_ad = (By.CLASS_NAME, 'item-list')
item = (By.CLASS_NAME, 'select2-selection__rendered')
input_item = (By.CLASS_NAME, 'select2-search__field')
button_show = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')
checkbox_photo = (By.NAME, 'js-photo')
checkbox_used = (By.NAME, 'js-isused')
found_number = (By.XPATH, '//b[text()="3"]')
found_number_with_photo = (By.XPATH, '//b[text()="2"]')
found_number_with_used = (By.XPATH, '//b[text()="0"]')
number_ad_of_mark = (By.CLASS_NAME, 'item-list')
ad_sort = (By.CLASS_NAME, 'select2-selection__arrow')
select_sort = (By.CLASS_NAME, 'select2-results__option')
ad1_cost = (By.XPATH, '//span[contains(.,"50")]')
ad2_cost = (By.XPATH, '//span[contains(.,"15")]')
ad1_old = (By.XPATH, '//a[contains(.,"к Богдан А092, 2000 г.")]')
ad2_old = (By.XPATH, '//a[contains(.,"к Богдан А092, 2003 г.")]')
ad_mark_correct = (By.XPATH, '//a[contains(.,"к Богдан А092, 2003 г.")]')
ad_model_correct = (By.XPATH, '//a[contains(.,"  к Богдан А092, 2003 г.  ")]')
ad_part_correct = (By.XPATH, '//b[contains(.,"Барабан тормозной")]')
ad = (By.CLASS_NAME, 'tmb-wrap-table')
mark_name = (By.CSS_SELECTOR, 'span[title="Богдан"]')
cross_abort = (By.CLASS_NAME, 'select2-selection__clear')
mark_name_clear = (By.CLASS_NAME, 'select2-selection__placeholder')
model_name = (By.CSS_SELECTOR, 'span[title="А092"]')
part_number = (By.ID, 'originalnum')
price_from = (By.XPATH, '//input[@id="price-ot"]')
price_to = (By.XPATH, '//input[@id="price-do"]')
seller_add = (By.XPATH, '//span[text()="продавец"]')
more_settings = (By.ID, 'js-more-params-link')
city = (By.XPATH, '//a[text()=" Минск"]')
value = (By.ID, 'enginevalue')
text_value = (By.XPATH, '//span[contains(.,"2.0 л")]')
text_fuel = (By.XPATH, '//span[contains(.,"бензин")]')
text_gear = (By.XPATH, '//span[contains(.,"АКПП")]')
text_body = (By.XPATH, '//span[contains(.,"седан")]')
artikul_number = (By.ID, 'artikul')
note = (By.XPATH, '//span[text()="Блокнот"]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://bamper.by/')

    def button_enter_click(self):
        self.find_element(button_enter).click()

    def button_next_click(self):
        self.find_element(button_next).click()

    def number_ad_on_page(self):
        return len(self.find_elements(number_ad))

    def button_show_click(self):
        return self.find_element(button_show).click()

    def mark_click(self):
        self.find_elements(item)[0].click()

    def model_click(self):
        self.find_elements(item)[1].click()

    def input_mark(self):
        self.find_element(input_item).send_keys('Богдан')

    def input_bmw(self):
        self.find_element(input_item).send_keys('BMW')

    def input_model(self):
        self.find_element(input_item).send_keys('А092')

    def year_from_click(self):
        self.find_elements(item)[2].click()

    def year_before_click(self):
        self.find_elements(item)[3].click()

    def part_click(self):
        self.find_elements(item)[4].click()

    def part_input(self):
        self.find_element(input_item).send_keys('Барабан тормозной')

    def seller_click(self):
        self.find_elements(item)[5].click()

    def seller_input(self):
        self.find_element(input_item).send_keys('4AVTO.by')

    def city_click(self):
        self.find_elements(item)[6].click()

    def city_input(self):
        self.find_element(input_item).send_keys('Минск')

    def fuel_click(self):
        self.find_elements(item)[7].click()

    def fuel_input(self):
        self.find_element(input_item).send_keys('бензин')

    def gear_click(self):
        self.find_elements(item)[8].click()

    def gear_input(self):
        self.find_element(input_item).send_keys('АКПП')

    def body_click(self):
        self.find_elements(item)[9].click()

    def body_input(self):
        self.find_element(input_item).send_keys('седан')

    def ad_part_correct(self):
        return self.find_element(ad_part_correct).text

    def year_from_input(self):
        self.find_element(input_item).send_keys('2001')

    def year_before_input(self):
        self.find_element(input_item).send_keys('2001')

    def year_f(self):
        self.find_element(input_item).send_keys('1999')

    def year_b(self):
        self.find_element(input_item).send_keys('1999')

    def part_num_correct(self):
        return self.find_element(part_number).text

    def part_number_click(self):
        self.find_element(part_number).click()

    def part_number_input(self):
        self.find_element(part_number).send_keys('8970339891')

    def part_input_number_incorrect(self):
        self.find_element(part_number).send_keys('---')

    def price_from_click(self):
        self.find_element(price_from).click()

    def price_from_input(self):
        self.find_element(price_from).send_keys('40')

    def price_to_click(self):
        self.find_element(price_to).click()

    def price_to_input(self):
        self.find_element(price_to).send_keys('60')

    def checkbox_with_photo_click(self):
        self.find_element(checkbox_photo).click()

    def checkbox_used_click(self):
        self.find_element(checkbox_used).click()

    def found_number(self):
        return int(self.find_element(found_number).text)

    def found_number_with_photo(self):
        return int(self.find_element(found_number_with_photo).text)

    def found_number_with_used(self):
        return int(self.find_element(found_number_with_used).text)

    def number_ad_select_mark(self):
        return len(self.find_elements(number_ad_of_mark))

    def ad_sort_click(self):
        self.find_elements(ad_sort)[-1].click()

    def reach_sort_click(self):
        self.find_elements(select_sort)[1].click()

    def older_sort_click(self):
        self.find_elements(select_sort)[5].click()

    def ad1_cost(self):
        num = []
        for i in self.find_element(ad1_cost).text:
            if i.isdigit():
                num.append(i)
        return int((''.join(num))[:2])

    def ad2_cost(self):
        num = []
        for i in self.find_element(ad2_cost).text:
            if i.isdigit():
                num.append(i)
        return int((''.join(num))[:2])

    def ad1_old(self):
        year = []
        for i in self.find_element(ad1_old).text:
            if i.isdigit():
                year.append(i)
        return int((''.join(year))[-4:])

    def ad2_old(self):
        year = []
        for i in self.find_element(ad2_old).text:
            if i.isdigit():
                year.append(i)
        return int((''.join(year))[-4:])

    def ad_mark_correct(self):
        if 'Богдан' in self.find_element(ad_mark_correct).text:
            mark = 'Богдан'
        else:
            mark = 'Не Богдан'
        return mark

    def mark_name(self):
        return self.find_element(mark_name).text[2:]

    def ad_cross_abort_click(self):
        self.find_element(cross_abort).click()

    def mark_name_clear(self):
        return self.find_elements(mark_name_clear)[0].text

    def input_model_click(self):
        self.find_element(model_name).send_keys('А092')

    def ad_model_correct(self):
        if 'А092' in self.find_element(ad_model_correct).text:
            model = 'А092'
        else:
            model = 'Не A092'
        return model

    def model_name(self):
        return self.find_element(model_name).text[2:]

    def ad_click(self):
        self.find_element(ad).click()

    def seller_add_displayed(self):
        return self.find_elements(seller_add)[-1].is_displayed()

    def more_settings_click(self):
        self.find_element(more_settings).click()

    def city_correct(self):
        for i in range(len(self.find_elements(number_ad))):
            if "Минск" in self.find_elements(city)[i].text:
                name = self.find_elements(city)[i].text
            else:
                name = "Не Минск"
            return name

    def engine_value_input(self):
        self.find_element(value).send_keys('2.0')

    def engine_value_text(self):
        for i in range(len(self.find_elements(number_ad))):
            if "2.0" in self.find_elements(text_value)[i].text:
                val = "2.0"
            else:
                val = "Не 2.0"
            return val

    def fuel_text(self):
        for i in range(len(self.find_elements(number_ad))):
            if "бензин" in self.find_elements(text_fuel)[i].text:
                fuel = "бензин"
            else:
                fuel = "Не бензин"
            return fuel

    def gear_text(self):
        for i in range(len(self.find_elements(number_ad))):
            if "АКПП" in self.find_elements(text_gear)[i].text:
                gear = "АКПП"
            else:
                gear = "Не АКПП"
            return gear

    def body_text(self):
        for i in range(len(self.find_elements(number_ad))):
            if "седан" in self.find_elements(text_body)[i].text:
                body = "седан"
            else:
                body = "Не седан"
            return body

    def artikul_number_click(self):
        self.find_element(artikul_number).click()

    def artikul_number_input(self):
        self.find_element(artikul_number).send_keys('8970339891')

    def note_click(self):
        self.find_element(note).click()
