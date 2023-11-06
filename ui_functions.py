import constants
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators import Google, StartAction, MainPage, CarSearchOptions, CarSuggestionsPage, CarSuggestionPage
import allure


class Webdriver:

    def __init__(self, driver):
        self.driver = driver

    def set_up_web(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    def click_java_script(self, web_element):
        time.sleep(1)
        element = self.find_element(*web_element)
        self.execute_script("arguments[0].click();", element)


class OpenWeb:

    @allure.step("Переходим на сайт СберЛизинг из поисковика браузера")
    def open_site_by_google_search(self):
        self.driver.get(constants.GOOGLE_PAGE)
        self.driver.find_element(*Google.GOOGLE_SEARCH_INPUT).send_keys('СберЛизинг\n')
        self.driver.find_element(*StartAction.SBERLEASING_LINK).click()
        self.driver.find_element(*StartAction.COOKIE_CLOSE_BUTTON).click()


class SberleasingMainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажимаем кнопку 'Подобрать по параметрам' и переходим на форму automall")
    def go_to_car_search_options(self):
        self.driver.find_element(*MainPage.CAR_SEARCH_OPTIONS_BUTTON).click()


class CarsSearchOptions:

    def __init__(self, driver, city_index, brand_index, model_index):
        self.driver = driver
        self.car = CarSearchOptions(city_index, brand_index, model_index)

    @allure.step("Устанавливаем чекбокс 'Только авто со скидкой'")
    def discount_checkbox_click(self):
        Webdriver.click_java_script(self.driver, CarSearchOptions.DISCOUNT_CHECKBOX)
        time.sleep(2)

    @allure.step("Выбираем Город  из списка")
    def set_city_option(self):
        self.driver.find_element(*CarSearchOptions.FILTER_CITY).click()
        self.driver.find_element(*self.car.get_city_choice_locator()).click()
        self.driver.find_element(*CarSearchOptions.FILTER_CITY).click()
        time.sleep(2)

    @allure.step("Выбираем Марку авто из списка")
    def set_brand_option(self):
        self.driver.find_element(*CarSearchOptions.FILTER_BRAND).click()
        self.driver.find_element(*self.car.get_brand_choice_locator()).click()
        self.driver.find_element(*CarSearchOptions.FILTER_BRAND).click()
        time.sleep(2)

    @allure.step("Определяем выбранную Марку авто")
    def get_filter_brand_choice(self):
        return (self.driver.find_element(*CarSearchOptions.FILTER_BRAND_CHOISE).get_attribute("textContent")).strip()

    @allure.step("Выбираем Модель авто из списка")
    def set_model_option(self):
        self.driver.find_element(*CarSearchOptions.FILTER_MODEL).click()
        self.driver.find_element(*self.car.get_model_choice_locator()).click()
        self.driver.find_element(*CarSearchOptions.FILTER_MODEL).click()
        time.sleep(2)

    @allure.step("Скролл блока выбора опций авто")
    def car_options_block_scroll(self):
        self.driver.find_element(*CarSearchOptions.FILTER_CITY).location_once_scrolled_into_view

    @allure.step("Указываем Мощность двигателя")
    def set_engine_power(self):
        slider = self.driver.find_element(*CarSearchOptions.ENGINE_POWER_MIN)
        slider.click()
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 3, 0).perform()

    @allure.step("Определяем активные чекбоксы фильтра Привод, при наличии выбираем первый")
    def set_transmission(self):
        active_checkboxes = self.driver.find_elements(*CarSearchOptions.ACTIVE_TRANSMISSION_CHECKBOXES)
        if len(active_checkboxes) > 0:
            FIRST_TRANSMISSION_CHECKBOX = (By.XPATH, '(//*[text()=" Привод "]/..//input[not(@disabled)])[1]')
            Webdriver.click_java_script(self.driver, FIRST_TRANSMISSION_CHECKBOX)

    @allure.step("Определяем активные чекбоксы фильтра Коробка передач, при наличии выбираем первый")
    def set_transmission_box(self):
        active_checkboxes = self.driver.find_elements(*CarSearchOptions.ACTIVE_TRANSMISSION_BOX_CHECKBOXES)
        if len(active_checkboxes) > 0:
            FIRST_TRANSMISSION_BOX_CHECKBOX = (By.XPATH,
                                               '(//*[text()=" Коробка передач "]/..//input[not(@disabled)])[1]')
            Webdriver.click_java_script(self.driver, FIRST_TRANSMISSION_BOX_CHECKBOX)

    @allure.step("Определяем активные чекбоксы фильтра Тип кузова, при наличии выбираем первый")
    def set_body_type(self):
        active_checkboxes = self.driver.find_elements(*CarSearchOptions.ACTIVE_BODY_TYPE_CHECKBOXES)
        if len(active_checkboxes) > 0:
            FIRST_ACTIVE_BODY_TYPE_CHECKBOXES = (By.XPATH, '(//*[text()=" Тип кузова "]/..//input[not(@disabled)])[1]'
                                                           '/..//*[@class="checkboxes-body-type__label"]')
            Webdriver.click_java_script(self.driver, FIRST_ACTIVE_BODY_TYPE_CHECKBOXES)

    @allure.step("Указываем Объём двигателя")
    def set_engine_capacity(self):
        slider = self.driver.find_element(*CarSearchOptions.ENGINE_CAPACITY_MAX)
        slider.click()
        ActionChains(self.driver).drag_and_drop_by_offset(slider, -162, 0).perform()

    @allure.step("Определяем активные чекбоксы фильтра Тип топлива, при наличии выбираем первый")
    def set_fuel_type(self):
        active_checkboxes = self.driver.find_elements(*CarSearchOptions.FUEL_TYPE_CHECKBOXES)
        if len(active_checkboxes) > 0:
            FIRST_FUEL_TYPE_CHECKBOX = (By.XPATH, '(//*[text()=" Тип топлива "]/..//input[not(@disabled)])[1]')
            Webdriver.click_java_script(self.driver, FIRST_FUEL_TYPE_CHECKBOX)

    @allure.step("Указываем Цвет авто: выбираем первое значение списка")
    def set_colour_option(self):
        self.driver.find_element(*CarSearchOptions.COLOUR_OPTION).click()
        FIRST_COLOUR = (By.XPATH, '(//*[text()=" Цвет "]/..//label[@class="sbl-filter-checkbox__title"])[1]')
        self.driver.find_element(*FIRST_COLOUR).click()
        time.sleep(1)

    @allure.step("Нажимаем кнопку Показать все предложения")
    def show_all(self):
        Webdriver.click_java_script(self.driver, CarSearchOptions.SHOW_ALL_BUTTON)
        time.sleep(1)


class CarSuggestionList:

    def __init__(self, driver, suggestion_index):
        self.driver = driver
        self.suggestion = CarSuggestionsPage(suggestion_index)

    @allure.step("Определяем Марку в общем списке предложений")
    def get_suggestion_list_brand(self):
        self.driver.find_element(*CarSuggestionsPage.SUGGESTION_LIST_BRAND).click()
        time.sleep(1)
        return (self.driver.find_element(*CarSuggestionsPage.SUGGESTION_LIST_BRAND_CHOICE).
                get_attribute("textContent")).strip()

    @allure.step("Выбираем предложение")
    def show_suggestion(self):
        self.driver.find_element(*self.suggestion.get_suggestion_choice_locator()).click()
        time.sleep(1)


class CarSuggestion:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем информацию по авто на странице предложения")
    def get_suggestion_info(self):
        return (self.driver.find_element(*CarSuggestionPage.SUGGESTION_CAR_INFO).get_attribute("innerText")).strip()
