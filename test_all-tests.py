from page.home_page import HomePage
from page.autorization_page import AutorizationPage
from page.ad_page import AdPage
from page.seller_page import SellerPage
from page.note_page import NotePage
from page.add_part_page import AddPartPage
from page.new_part_page import NewPartPage
from page.list_ad_page import ListAdPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep
import allure


"""
Запуск тестов:
pytest --reruns 2 --alluredir=D:/diplom-qap05/allure-reports
allure serve D:/diplom-qap05/allure-reports
"""


@allure.feature('Логин')
@allure.story('Логин пользователя')
def test_login(driver):
    with allure.step('Открываю домашнюю страницу'):
        home_page = HomePage(driver)
        home_page.open()
        home_page.button_enter_click()
        autorization = AutorizationPage(driver)
    with allure.step('Авторизируюсь'):
        autorization.login()
        autorization.password()
        autorization.button_login_click()
        assert driver.current_url == "https://bamper.by/personal/?login=yes"


@allure.feature('Следующая страница объявлений')
def test_button_next(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.button_next_click()
    assert driver.current_url == "https://bamper.by/?PAGEN_1=2"


@allure.feature('Количество объявлений на странице')
def test_number_ad_on_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    assert home_page.number_ad_on_page() == 20


@allure.feature('Количество объявлений по марке')
def test_number_select_ad_by_mark(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    assert home_page.found_number() == home_page.number_ad_select_mark()


@allure.feature('Фильтр - объявления с фото')
def test_number_found_ad_filter_with_photo(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    home_page.checkbox_with_photo_click()
    home_page.button_show_click()
    assert home_page.found_number_with_photo() == home_page.number_ad_select_mark()


@allure.feature('Фильтр - объявления б/у')
def test_number_found_ad_filter_used(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    home_page.checkbox_used_click()
    home_page.button_show_click()
    assert home_page.found_number_with_used() == home_page.number_ad_select_mark()


@allure.feature('Фильтр - цена по убыванию')
def test_order_cheap(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    home_page.ad_sort_click()
    home_page.reach_sort_click()
    assert home_page.ad1_cost() > home_page.ad2_cost()


@allure.feature('Фильтр - год по возрастанию')
def test_order_older(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    home_page.ad_sort_click()
    home_page.older_sort_click()
    assert home_page.ad1_old() < home_page.ad2_old()


@allure.feature('Выбор марки')
def test_mark_correct(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    assert home_page.ad_mark_correct() == home_page.mark_name()


@allure.feature('Выбор марки - отмена выбора')
def test_ad_abort(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    home_page.ad_cross_abort_click()
    assert home_page.mark_name_clear() == 'марка а/м'


@allure.feature('Выбор модели')
def test_model_correct(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.model_click()
    home_page.input_model()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    assert home_page.ad_model_correct() == home_page.model_name()


@allure.feature('Выбор от какого года')
def test_year_from(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.year_from_click()
    home_page.year_from_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    assert home_page.number_ad_on_page() == 1


@allure.feature('Выбор до какого года')
def test_year_before(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.year_before_click()
    home_page.year_before_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    sleep(2)
    assert home_page.number_ad_on_page() == 2


@allure.feature('Выбор года')
def test_year(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.year_from_click()
    home_page.year_f()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.year_before_click()
    home_page.year_b()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    sleep(2)
    assert home_page.number_ad_on_page() == 0


@allure.feature('Номер(код) запчасти')
def test_part_number(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.part_number_click()
    home_page.part_number_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    assert home_page.number_ad_on_page() == 1


@allure.feature('Номер(код) запчасти - коррекция ввода')
def test_part_number_correct(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.part_number_click()
    home_page.part_input_number_incorrect()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    assert home_page.part_num_correct() == ''


@allure.feature('Запчасть')
def test_part(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.part_click()
    home_page.part_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    sleep(2)
    assert home_page.ad_part_correct() == 'Барабан тормозной'


@allure.feature('Продавец')
def test_seller(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.seller_click()
    home_page.seller_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    home_page.ad_click()
    driver.switch_to.window(driver.window_handles[1])
    ad_page = AdPage(driver)
    ad_page.seller_click()
    driver.switch_to.window(driver.window_handles[2])
    seller_page = SellerPage(driver)
    name = seller_page.seller_name()
    assert name == '4AVTO.by'


@allure.feature('Стоимость - цена от')
def test_price_from(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.price_from_click()
    home_page.price_from_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    assert home_page.ad1_cost() > 40


@allure.feature('Стоимость - цена до')
def test_price_to(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.price_to_click()
    home_page.price_to_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    assert home_page.ad1_cost() < 60


@allure.feature('Стоимость - диапазон цен')
def test_price_from_to(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.price_from_click()
    home_page.price_from_input()
    home_page.price_to_click()
    home_page.price_to_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    assert home_page.ad1_cost() > 40
    assert home_page.ad1_cost() < 60


@allure.feature('Добавление дополнительного продавца')
def test_seller_add(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.seller_click()
    home_page.seller_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    sleep(2)
    assert home_page.seller_add_displayed() is True


@allure.feature('Выбор города')
def test_city(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.more_settings_click()
    home_page.city_click()
    home_page.city_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    sleep(2)
    assert home_page.city_correct() == "Минск"


@allure.feature('Фильтр - объем двигателя')
def test_value(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_bmw()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.more_settings_click()
    home_page.engine_value_input()
    home_page.button_show_click()
    assert home_page.engine_value_text() == "2.0"


@allure.feature('Фильтр - тип топлива')
def test_fuel(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_bmw()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.more_settings_click()
    home_page.fuel_click()
    home_page.fuel_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    sleep(2)
    assert home_page.fuel_text() == "бензин"


@allure.feature('Фильтр - тип коробки передач')
def test_gear(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_bmw()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.more_settings_click()
    home_page.gear_click()
    home_page.gear_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    sleep(2)
    assert home_page.gear_text() == "АКПП"


@allure.feature('Фильтр - тип кузова')
def test_body(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_bmw()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.more_settings_click()
    home_page.body_click()
    home_page.body_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    sleep(2)
    assert home_page.body_text() == "седан"


@allure.feature('Номер артикула')
def test_artikul_number(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.more_settings_click()
    home_page.artikul_number_click()
    home_page.artikul_number_input()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    assert home_page.number_ad_on_page() == 1


@allure.feature('Маркировка объявления - добавление в блокнот')
def test_note(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    sleep(2)
    home_page.button_show_click()
    home_page.ad_click()
    driver.switch_to.window(driver.window_handles[1])
    ad_page = AdPage(driver)
    ad_page.add_to_note_click()
    driver.switch_to.window(driver.window_handles[0])
    home_page.note_click()
    note_page = NotePage(driver)
    assert note_page.ad_in_note() == "Барабан тормозной к Богдан А092, 2003 г."


@allure.feature('Очистка блокнота')
def test_clear_note(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.mark_click()
    home_page.input_mark()
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    home_page.button_show_click()
    home_page.ad_click()
    driver.switch_to.window(driver.window_handles[1])
    ad_page = AdPage(driver)
    ad_page.add_to_note_click()
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    home_page.note_click()
    note_page = NotePage(driver)
    note_page.button_clear_note_click()
    sleep(2)
    assert note_page.note_text() == "Нет объявлений в блокноте"


@allure.feature('Добавление объявления')
@allure.story('Запчасть - Эмблема')
def test_add_ad(driver):
    with allure.step('Открываю домашнюю страницу'):
        home_page = HomePage(driver)
        home_page.open()
        home_page.button_enter_click()
    with allure.step('Авторизируюсь'):
        autorization = AutorizationPage(driver)
        autorization.login()
        autorization.password()
        autorization.button_login_click()
    with allure.step('Открываю страницу добавления объявления'):
        add_part = AddPartPage(driver)
        add_part.add_ad_button_click()
    with allure.step('Открываю страницу заполнения полей'):
        new_part = NewPartPage(driver)
        new_part.mark_select()
        new_part.model_select()
        new_part.year_input()
        new_part.part_select()
        new_part.flag_click()
        new_part.cost_input()
        new_part.activation_click()
        new_part.save_ad_click()
    with allure.step('Открываю страницу списка объявлений'):
        new_part.all_ad_click()
        driver.switch_to.window(driver.window_handles[1])
        list_ad = ListAdPage(driver)
        assert list_ad.num_ad() == '1'


@allure.feature('Удаление объявления')
def test_delete_ad(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.button_enter_click()
    autorization = AutorizationPage(driver)
    autorization.login()
    autorization.password()
    autorization.button_login_click()
    add_part = AddPartPage(driver)
    add_part.my_ad_click()
    list_ad = ListAdPage(driver)
    list_ad.delete_ad_click()
    sleep(2)
    Alert(driver).accept()
    sleep(5)
    assert list_ad.text_ad() is True


@allure.feature('Корректность отображения количества объявлений после удаления')
def test_num_ad(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.button_enter_click()
    autorization = AutorizationPage(driver)
    autorization.login()
    autorization.password()
    autorization.button_login_click()
    add_part = AddPartPage(driver)
    add_part.add_ad_button_click()
    new_part = NewPartPage(driver)
    new_part.mark_select()
    new_part.model_select()
    new_part.year_input()
    new_part.part_select()
    new_part.flag_click()
    new_part.cost_input()
    new_part.activation_click()
    new_part.save_ad_click()
    new_part.all_ad_click()
    driver.switch_to.window(driver.window_handles[1])
    list_ad = ListAdPage(driver)
    list_ad.delete_ad_click()
    sleep(2)
    Alert(driver).accept()
    sleep(2)
    """
    Счетчик объявлений обнуляется только после обновления страницы
    Без рефреша - BUG
    """
    # driver.refresh()
    # sleep(2)
    assert list_ad.num_ad() == '0'
