import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from base.base_class import Base


# Класс для формы с фильтрами

class selection_telescope(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    price_slider_left = (By.XPATH, "//a[@class='ui-slider-handle ui-state-default ui-corner-all']")

    price_slider_right_window = (By.XPATH, "//input[@id='maxCost']")

    check_box_sky_sturman = (By.XPATH, "//*[contains(text(), 'STURMAN (Штурман)')]")

    # Выпадашка, все бренды
    all_brends = (By.XPATH, "//span[@class='links more-button']")

    # Выпадашка, по уровню подготовки
    # by_level_of_training = (By.XPATH, "//p[@class='left-menu-title-head'][3]")

    # Кнопка выбрать параметры фильтров
    input_button = (By.XPATH, "//input[@class='left-menu-go-button']")
    by_children = (By.XPATH, "//span[@id='user_level_1']")

    # Getter
    def get_select_by_price_windiw_right(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.price_slider_right_window))

    def get_select_by_price_slider_left(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.price_slider_left))

    def get_select_check_box_sturman(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.check_box_sky_sturman))

    def get_select_all_brends(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.all_brends))

    # def get_select_by_level_of_training(self):
    #
    #     return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.by_level_of_training))

    def get_select_input_button(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.input_button))

    def get_select_by_children(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.by_children))

    # Action
    def click_price_widow_right(self):
        # Прописываем сумму в поле ввода
        self.get_select_by_price_windiw_right().clear()
        self.get_select_by_price_windiw_right().send_keys("16000")
        self.get_select_by_price_windiw_right().send_keys(Keys.ENTER)

        print("Прописываем сумму в правое окошко")

    def click_price_slider_left(self):
        # Взаимодействие с ползунком с помощью мыши
        action = ActionChains(self.driver)

        # click_and_hold - кликаем и тянем, move_by_offset- на какое расстояние тянем, горизонт и вертикаль,
        # release - отпускаем, perform - сохраняем, то что сделали) Пока тестил нашёл баг у левого ползунка =)

        action.click_and_hold(self.get_select_by_price_slider_left()).move_by_offset(90, 90).release().perform()
        print("Тянем бегунок вправо на нужное нам значение")

    def click_all_brends(self):
        self.get_select_all_brends().click()
        print("Кликаем на кнопку 'все бренды'")

    def click_check_box_sturman(self):
        self.get_select_check_box_sturman().click()
        print("Кликаем на чек-бокс 'STURMAN'")

    def click_input_button(self):
        self.get_select_input_button().click()
        print("Кликаем на кнопку 'Выбрать'")

    def click_by_children(self):
        self.get_select_by_children().click()
        print("Кликаем на чек-бокс 'Для детей'")

    # Данный метод настраивает фильтры для поиска и нажимаем кнопку выбрать, что произошёл отбор телескоп
    # по интересующим нам параметрам
    def telescope_selection(self):
        self.click_price_slider_left()
        self.click_price_widow_right()
        self.click_all_brends()
        self.scrolling()
        self.click_check_box_sturman()
        self.click_by_children()

        self.click_input_button()

        time.sleep(3)
        self.get_current_url()
        self.assert_url("https://www.4glaza.ru/katalog/teleskopy/sturman/?user_level=1&to_price=16000")
        time.sleep(3)
