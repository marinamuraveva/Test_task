import pytest
import unittest
from ui_functions import Webdriver, OpenWeb, SberleasingMainPage, CarsSearchOptions, CarSuggestionList, CarSuggestion
import allure


class UiTests(unittest.TestCase):
    def setUp(self):
        self.driver = Webdriver.set_up_web(self)

    @allure.title("Проверяем соответствие выбранной марки авто марке в общем списке")
    def test_car_brand_matching(self):
        with allure.step("Находим Sberleasing через поиск Google, переходим на страницу с фильтрами"):
            OpenWeb.open_site_by_google_search(self)
            main_page = SberleasingMainPage(self.driver)
            main_page.go_to_car_search_options()

        with allure.step("Задаем порядковый номер в списке выбора города, марки и модели"):
            cars = CarsSearchOptions(self.driver, city_index=2, brand_index=1, model_index=1)

        with allure.step("Указываем параметры отбора Дисконт, Город и Марка"):
            cars.discount_checkbox_click()
            cars.set_city_option()
            cars.set_brand_option()

        with allure.step("Определям указанную в фильтре Марку"):
            filter_brand_choice = cars.get_filter_brand_choice()

        with allure.step("Указываем остальные параметры отбора"):
            cars.set_model_option()
            cars.car_options_block_scroll()
            cars.set_engine_power()
            cars.set_transmission()
            cars.set_transmission_box()
            cars.set_body_type()
            cars.set_fuel_type()
            cars.set_colour_option()
            cars.set_engine_capacity()

        with allure.step("Переходим на страницу Результатов подбора авто"):
            cars.show_all()

        with allure.step("Задаем порядковый номер предложения в списке"):
            suggestion_list = CarSuggestionList(self.driver, suggestion_index=1)

        with allure.step("Определяем Марку в общем списке предложений и переходим в конкретное предложение"):
            suggestion_list_brand = suggestion_list.get_suggestion_list_brand()
            suggestion_list.show_suggestion()

        with allure.step("Получаем инфо по авто на странице предложения"):
            suggestion = CarSuggestion(self.driver)
            suggestion_info = suggestion.get_suggestion_info()

        with allure.step("Проверяем, что Марка авто на фильтрах, в списке предложений "
                         "и на странице предложения совпадает"):
            assert filter_brand_choice == suggestion_list_brand,\
                'Марка авто на фильтрах не совпадает с маркой авто в списке предложений'
            assert suggestion_list_brand in suggestion_info, \
                'Марка авто в списке предложений не совпадает с маркой авто на странице предложения'