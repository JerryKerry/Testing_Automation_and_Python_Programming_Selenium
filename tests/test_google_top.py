from pages.top_page import Top_page


def test_google_top(driver):
    print("Выполняется тест - 'Проверка сайта в топе google'")

    tp = Top_page(driver)
    tp.search()
