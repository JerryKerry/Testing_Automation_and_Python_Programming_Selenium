import pytest
import allure


from pages.login_page import Login_Page

@allure.description('Тест авторизации пользователя')
def test_authorization(driver, set_up, set_group):
    print("Выполняется тест - 'Авторизация пользователя'")

    ta = Login_Page(driver)

    ta.authorization()
    ta.click_get_out()

# Пришлось прописывать в терминале pip3 install pytest-ordering, что тесты запускались последовательно

@pytest.mark.run(order=1)
# Тест для отработки фикстуры
def test_fixture(driver):

    ta = Login_Page(driver)
    ta.test()
