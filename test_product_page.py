import pytest
from pages.product_page import ProductPage
import time


@pytest.mark.parametrize('links', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3", "?promo=offer4",
                                   "?promo=offer5", "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_link()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_message()
    page.should_match_titles_of_add_to_basket_message_and_product()
    page.should_be_basket_price_message()
    page.should_match_prices_of_basket_message_and_product()
