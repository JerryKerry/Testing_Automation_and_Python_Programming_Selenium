from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

from base.base_class import Base


# Главная страница сайта
class telescope_menu(Base):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # Locators
    # Меню телескопы
    telescope_menu_locator = (By.XPATH, "//a[text()='Телескопы']")

    # Getter
    def get_select_telescope_menu(self):
        return WebDriverWait(self.driver, 50).until(ES.element_to_be_clickable(self.telescope_menu_locator))

    # Action
    def click_telescope_menu(self):
        self.get_select_telescope_menu().click()

        print("Кликаем в меню на 'телескопы'")

    # Кликаем на меню
    def click_menu_telescope(self):
        self.click_telescope_menu()
