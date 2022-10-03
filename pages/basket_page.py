from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Empty Basket Message is not ' \
                                                                                    'presented '

    def should_not_be_item_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "The item is presented on the Basket Page"
