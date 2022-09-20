# Класс хранит экземпляр драйвера Хром
# Расширяется универсальными методами, которые будут выполняться в каждом тесте
import datetime
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Метод показывает текущий url страницы
    def get_current_url(self):
        get_url = self.driver.current_url
        print('url = ' + get_url)

    # Метод сравнивает текущий url с переданным в параметр функции
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Данный url верный')

    # Парсим  страницу для подтверждения
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result


    # Метод скриншота

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'name_screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects'
                                    '\\Testing_Automation_and_Python_Programming_Selenium\\screen\\' + name_screenshot)
        print("Делаем скриншот")
    # Метод перехода по заданному url
    def get_go_url(self, url):
        self.driver.get(url)

    # Возрващаемся в браузере назад
    def get_back(self):
        self.driver.back()


    def scrolling(self):
        self.driver.execute_script('window.scrollTo(0, 500)')
        time.sleep(3)
        print("scrolling")
