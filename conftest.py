import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
"""функция которая создаёт драйвер, открывает его и после выполнения теста закрывает"""

# """Команда запускает браузер при запуске функции тест кейса"""
@pytest.fixture(scope='session')
def driver():

    # Игнорирование ошибок в терминале, некоторые сохранил на всякий случай

    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    s = Service('C:\\Users\\user\\PycharmProjects\\python_selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=s,options=options)

    driver.maximize_window()
    print("Стартуем")

    yield driver
    driver.quit()



# Прописывает название функции в параметры нужной функции, фикстуры написаны для показателной работы
@pytest.fixture()
def set_up():
    print('Отрабатывает фикстура set_up')
    # Тут проходит тест

    yield

    # В конце каждого теста
    print('\nФиниш фикстуры\n')


@pytest.fixture(scope="module")
def set_group():
    print('Старт фикстуры для модуля ')
    # Тут проходит тест

    yield

    # В конце каждого теста
    print('\nФикстура для модуля отработала')
