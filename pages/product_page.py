from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    def should_be_product_link(self):
        self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Product page URL is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add To Basket Button is not presented"

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Add To Basket Message is not presented"

    def should_match_titles_of_add_to_basket_message_and_product(self):
        title_of_product = self.browser.find_element(*ProductPageLocators.TITLE_OF_PRODUCT).text
        basket_message_product_name = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_NAME).text
        assert title_of_product == basket_message_product_name, "Title of product doesn't match with title of Add To Basket Message"

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_MESSAGE),  "Price Basket Message is not presented"

    def should_match_prices_of_basket_message_and_product(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        basket_message_product_price = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_PRICE).text
        assert price_of_product == basket_message_product_price, "Price of product doesn't match with price of Basket Price Message"
