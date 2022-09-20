from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from base.base_class import Base


class cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Количество товара
    amount = (By.XPATH, "//input[@name='3234']")
    # Цена
    price = (By.XPATH, "//td[@class='cart-product-price']")
    # Сумма товара
    sum = (By.XPATH, "//td[@class='cart-product-summ]")
    # Наименование товара
    product_1 = (By.XPATH, "//a[text()='Телескоп STURMAN F36050 М']")
    # Кнопка оформить заказ
    cart_checkout_go = (By.XPATH, "//div[@id='cart-checkout-go']")

    def get_select_amount(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.amount))

    def get_select_price(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.price))

    def get_select_sum(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.sum))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.product_1))

    def get_select_cart_checkout_go(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.cart_checkout_go))



    def assert_amount(self):
        self.assert_word(self.get_select_amount(), '1')

    def click_cart_checkout(self):
        self.get_select_cart_checkout_go().click()


