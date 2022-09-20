from pages.login_page import Login_Page
from pages.base_page import telescope_menu


def test_telescope_menu(driver):
    print("Выполняется тест - 'Авторизация пользователя'")
    ta = Login_Page(driver)
    ta.authorization()

    tm = telescope_menu(driver)
    tm.click_menu_telescope()
