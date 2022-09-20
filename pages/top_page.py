from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as ES


# метод search будет искать наш сайт в гугле,
# а метод google_top проверять, что наш сайт находится на первом месте,
# фиксируя это скриншотом

class Top_page(Base):
    def __init__(self, driver):
        super().__init__(driver)




    input_google = (By.XPATH, "//input[@class='gLFyf gsfi']")
    google_search = (By.XPATH, "//div[@class='FPdoLc lJ9FBc']/center/input[@class='gNO89b']")

    # Getter
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(ES.element_to_be_clickable(self.input_google))

    def click_search(self):
        return WebDriverWait(self.driver, 30).until((ES.element_to_be_clickable(self.google_search)))




    def search(self):
        self.get_go_url('https://www.google.com/')
        self.get_current_url()
        self.get_user_name().send_keys('Четыре Глаза')
        self.get_user_name().send_keys(Keys.ENTER)
        self.get_screenshot()
        self.driver.quit()
