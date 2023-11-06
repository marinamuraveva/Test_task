from selenium.webdriver.common.by import By


class Google(object):
    '''Поисковая строка'''
    GOOGLE_SEARCH_INPUT = (By.XPATH, '//*[@type="search"]')


class StartAction(object):
    '''Ссылка на сайт СберЛизинга'''
    SBERLEASING_LINK = (By.XPATH, '//*[@href="https://www.sberleasing.ru/"]')
    '''Кнопка закрытия баннера куки'''
    COOKIE_CLOSE_BUTTON = (By.XPATH,  '//div[contains(text(), "«Сбербанк Лизинг» использует cookie")]/../button')


class MainPage(object):
    '''Кнопка Подобрать по параметрам'''
    CAR_SEARCH_OPTIONS_BUTTON = (By.XPATH, '//div[contains(@class, "text-right")]/*[contains(@href, "marketplace")]')


class CarSearchOptions(object):

    def __init__(self, city_index, brand_index, model_index):
        self.city_index = city_index
        self.brand_index = brand_index
        self.model_index = model_index

    '''Чекбокс Только авто со скидкой'''
    DISCOUNT_CHECKBOX = (By.XPATH, '//*[text()="Только авто со скидкой"]/../input')

    '''Фильтр Город'''
    FILTER_CITY = (By.XPATH, '//*[@id="filter-city"]/input')

    '''Чекбокс выбора города'''
    def get_city_choice_locator(self):
        return (By.XPATH,
                f'//*[@id="filter-city"]/input/../following-sibling::div//div[@role="option"][{self.city_index}]')

    '''Фильтр Бренд'''
    FILTER_BRAND = (By.XPATH, '//*[@id="filter-mark"]/input')

    '''Фильтр Бренд с выбранным значением'''
    FILTER_BRAND_CHOISE = (By.XPATH, '//*[@id="filter-mark"]/span')

    '''Чекбокс выбора Марки авто'''
    def get_brand_choice_locator(self):
        return (By.XPATH,
                f'//*[@id="filter-mark"]/input/../following-sibling::div//div[@role="option"][{self.brand_index}]')

    '''Фильтр Модель'''
    FILTER_MODEL = (By.XPATH, '//*[@id="filter-model"]/input')

    '''Чекбокс выбора Модели авто'''
    def get_model_choice_locator(self):
        return (By.XPATH,
                f'//*[@id="filter-model"]/input/../following-sibling::div//div[@role="option"][{self.model_index}]')

    '''Ползунок нижней границы значения Мощности двигателя'''
    ENGINE_POWER_MIN = (By.XPATH, '(//div[text()=" Мощность двигателя "]/..'
                                  '//*[contains(@class, "button el-tooltip__trigger")])[1]')

    '''Массив всех активных чекбокосов фильтра Привод'''
    ACTIVE_TRANSMISSION_CHECKBOXES = (By.XPATH, '//*[text()=" Привод "]/..//input[not(@disabled)]')

    '''Массив всех активных чекбокосов фильтра Коробка передач'''
    ACTIVE_TRANSMISSION_BOX_CHECKBOXES = (By.XPATH, '//*[text()=" Коробка передач "]/..//input[not(@disabled)]')

    '''Массив всех активных чекбокосов фильтра Тип кузова'''
    ACTIVE_BODY_TYPE_CHECKBOXES = (By.XPATH, '//*[text()=" Тип кузова "]/..//input[not(@disabled)]')

    '''Ползунок верхней границы Объёма двигателя'''
    ENGINE_CAPACITY_MAX = (By.XPATH, '(//div[text()=" Объём двигателя "]/..'
                                     '//*[contains(@class, "button el-tooltip__trigger")])[2]')

    '''Массив всех активных чекбокосов фильтра Тип кузова'''
    FUEL_TYPE_CHECKBOXES = (By.XPATH, '//*[text()=" Тип топлива "]/..//input[not(@disabled)]')

    '''Фильтр Цвет'''
    COLOUR_OPTION = (By.XPATH, '//*[text()=" Цвет "]/..//input[@placeholder]')

    '''Кнопка Показать все предложения'''
    SHOW_ALL_BUTTON = (By.XPATH, '//*[text()=" Показать все предложения "]')


class CarSuggestionsPage(object):

    def __init__(self, suggestion_index):
        self.suggestion_index = suggestion_index

    '''Выбранное предложение по авто'''
    def get_suggestion_choice_locator(self):
        return (By.XPATH,
                f'(//*[contains(text(),"Смотреть предложения")])[{self.suggestion_index}]')

    '''Фильтр 'Модель' в общем списке предложений'''
    SUGGESTION_LIST_BRAND = (By.XPATH, '//div[text()="Марка"]')

    '''Выбранная Марка авто в общем списке предложений'''
    SUGGESTION_LIST_BRAND_CHOICE = (By.XPATH, '//div[text()="Марка"]/../..//label')


class CarSuggestionPage(object):

    '''Заголовок с информацией по авто на странице предложения'''
    SUGGESTION_CAR_INFO = (By.XPATH, '//*[@class="h2"]')
