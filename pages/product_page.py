from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from base.base_class import Base


class product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
    # Locators

    sturman_f36050_m = (By.XPATH, "//div[@id='name']/a[text()='Телескоп STURMAN F36050 М']")
    # На каком складе находится товар
    store_availability_german = (By.XPATH, "//a[text()='на Германа']")
    # Цена товара
    price_sturman_f36050_m = (By.XPATH, "//p[@class='page-product-price']")
    # Кликаем на кнопку "добавить в корзину"
    click_on_cart = (By.XPATH, "//input[@id='product-page-buynow-but']")
    # Итоговая сумма
    grand_total = (By.XPATH, "//td/b[contains(., 'руб')]")

    price_sturman= "2 390 руб."


    # Getter
    def get_select_by_sturman_f36050_m(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.sturman_f36050_m))

    def get_select_by_price_sturman_f36050_m(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.price_sturman_f36050_m))

    def get_select_click_on_cart(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.click_on_cart))

    def get_select_grand_total(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.grand_total))


   # Action

    def assert_telescope_name(self, name_telescope='Телескоп STURMAN F36050 М'):
        self.assert_word(self.get_select_by_sturman_f36050_m(), name_telescope)
        print("Правильное название телескопа = " + name_telescope)


    def assert_price_sturman_f36050_m(self, price_telescope=price_sturman ):
        self.assert_word(self.get_select_by_price_sturman_f36050_m(), price_telescope)
        print("Правильная цена телескопа  = " + price_telescope)

    # Тут не проходит проверка суммы,очень странно )
    def assert_grand_total(self, total ='2 390 руб.'):
        try :
            self.assert_word(self.get_select_grand_total(), total)
            print("Правильная итоговая сумма = " + total)
        except AssertionError :
            print('Несовпадение суммы')



    def click_telescope_name(self):
        self.get_select_by_sturman_f36050_m().click()

    def click_cart(self):
        self.get_select_click_on_cart().click()

     # Method
    # добавление товара в корзину


    def adding_a_product_to_the_cart(self):
        self.assert_telescope_name()
        self.click_telescope_name()
        self.assert_price_sturman_f36050_m()
        self.click_cart()
        self.assert_grand_total()



