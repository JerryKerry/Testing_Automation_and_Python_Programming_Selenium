from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from base.base_class import Base


class order_form_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # ФИО и контактный номер берутся из лк, их заполнять не нужно
    select_stateCode = (By.XPATH , "//select[@id='stateCode']")
    stateCode = (By.XPATH , "//option[@value='city--sankt-peterburg']")

    select_city = (By.XPATH, "//select[@id='Ecom_BillTo_Postal_City']")
    city =(By.XPATH , "//select[@name='Ecom_BillTo_Postal_City']//option[@value='city--sankt-peterburg']")
    Postal_Street =(By.XPATH,"//input[@name='Ecom_BillTo_Postal_Street_Line1']")

    select_metro = (By.XPATH, "//select[@id='metro']")
    metro = (By.XPATH, "//select[@id='metro']/option[@value='Крестовский остров']")
    address = (By.XPATH , "//input[@name='Ecom_BillTo_Postal_Street_Line1']")
    delivery_method = (By.XPATH , "//input[@value='3']")
    card_payment = (By.XPATH , "//input[@id='cc']")
    comment = (By.XPATH , "//textarea[@id='order-comment-ch']")





    # Способ доставки



    # Getter



    def get_select_select_stateCode(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.select_stateCode))

    def get_stateCode(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.stateCode))

    def get_select_city(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.select_city))

    def get_city(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.city))

    def get_select_Postal_Street(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.Postal_Street))

    def get_select_metro(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.select_metro))

    def get_metro(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.metro))

    def get_select_address(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.address))

    def get_delivery_method(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.delivery_method))

    def get_select_card_payment(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.card_payment))

    def get_select_comment(self):
        return WebDriverWait(self.driver, 50).until(ES.visibility_of_element_located(self.comment))


    # Action



    def input_select_stateCode(self):
        self.get_select_select_stateCode().click()
        print("клик на список область\регион")

    def input_stateCode(self):
        self.get_stateCode().click()
        print("выбор города")


    def input_city(self):
        self.get_city().click()
        print("клик на список городов")

    def input_Postal_Street(self):
        self.get_select_Postal_Street().click()
        print("выбор города")


    def click_select_metro(self):
        self.get_select_metro().click()
        print("клик на список метро")

    def click_metro(self):
        self.get_metro().click()
        print("выбор метро")



    def click_delivery_method(self):
        self.get_delivery_method().click()
        print("выбор способа доставки")

    def click_card_payment(self):
        self.get_select_card_payment().click()
        print("выбор способа оплаты")

    def input_comment(self):
        self.get_select_comment().send_keys("Побыстрее")
        print("ввод комментария")



    # Method

    def contact_information(self):
        self.input_select_stateCode()
        self.input_stateCode()
        self.input_city()
        self.input_Postal_Street()
        self.click_metro()

        self.click_delivery_method()
        self.click_card_payment()
        self.input_comment()
        self.get_screenshot()
