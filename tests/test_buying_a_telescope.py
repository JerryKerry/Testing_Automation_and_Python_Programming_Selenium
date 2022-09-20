

from pages.login_page import Login_Page
from pages.base_page import telescope_menu
from pages.telescope_selections_page import selection_telescope
from pages.product_page import product_page
from pages.order_form_page import order_form_page
from pages.cart_page import cart_page



def test_telescope_menu(driver):
    print("Выполняется тест - 'Выбор и добавление товара в корзину'")
    ta = Login_Page(driver)
    ta.authorization()

    tm = telescope_menu(driver)
    tm.click_menu_telescope()

    st = selection_telescope(driver)
    st.telescope_selection()

    pg = product_page(driver)
    pg.adding_a_product_to_the_cart()

    cp = cart_page(driver)
    cp.click_cart_checkout()

    ofp = order_form_page(driver)
    ofp.Contact_Information()









