import time
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_class import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES


# Тут происходит авторизация,тест регистрации написать не удалось, тк стоит защита в виде ввода проверочного
# кода сгенерированного при загрузке страницы
from utilities.logger import Logger


class Login_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Locators

    # Локаторы формы авторизации
    # Вход
    input = (By.XPATH, "//a[@id='login']")
    # Поля логина и пароля
    loginEmail = (By.XPATH, "//input[@name='loginEmail']")
    password = (By.XPATH, "//input[@name='password']")
    # Кнопка Выход
    out = (By.XPATH, "//div[@class='account-quit']//a[@id='out_btn']")
    # Кнопка войти
    input_lk = (By.XPATH, "//input[@class='flatbtn-orange']")
    # Локатор слова после авторизации
    main_word = (By.XPATH, "//span[@id='acc-name-my']")

    # Getter
    def get_select_input(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable(self.input))

    def get_select_loginEmail(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable(self.loginEmail))

    def get_select_password(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable(self.password))

    def get_select_out(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable(self.out))

    def get_select_input_lk(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable(self.input_lk))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(ES.visibility_of_element_located(self.main_word))

    # Action

    def click_mouse_right(self):
        action = ActionChains(self.driver)
        right_click = self.get_main_word()
        action.context_click(right_click).perform()
        print("Правая кнопка мыши")

    def refresh(self):
        self.driver.refresh()
        print('Перезагрузка страницы')

    def click_input(self):
        self.get_select_input().click()
        print("Кликаем на кнопку вход")

    def input_loginEmail(self, login):
        self.get_select_loginEmail().send_keys(login)
        print("Ввод логина")

    def input_password(self, password):
        self.get_select_password().send_keys(password)
        print("Ввод пароля")

    def click_input_lk(self):
        self.get_select_input_lk().click()
        print("Нажимаем кнопку 'войти'")

    def get_out(self):
        self.get_select_out().click()
        print('Нажимаем выход')

    def get_back(self):
        self.driver.back()
        print('Назад по истории браузера')

    def get_forward(self):
        self.driver.forward()
        print('Вперед по истории браузера')

    # Method
    def authorization(self):
        with allure.step('Прохождение авторизации '):
            # Добавляем метод из класса, чтобы создать лог до начала выполнения метода
            Logger.add_start_step(method="authorization")
            self.get_go_url('https://www.google.com/')
            self.get_back()
            self.get_forward()
            self.driver.get('https://www.4glaza.ru/')
            self.get_screenshot()
            self.click_input()
            self.input_loginEmail('')
            self.input_password('')
            self.click_input_lk()
            self.assert_word(self.get_main_word(), 'зарегистрированный пользователь!')
            self.click_mouse_right()
            self.get_screenshot()
            self.get_main_word().click()
            self.refresh()
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
            # чтобы создать лог после выполнения метода


    def click_get_out(self):
        with allure.step('Выход из лк'):
            self.get_out()
    # Метод для теста отработки фикстуры =)
    def test(self):
        self.get_go_url('https://www.google.com/')
        time.sleep(3)
        self.get_screenshot()
