from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1) div.alertinner")
    BASKET_MESSAGE_PRODUCT_NAME = (By.XPATH, "//div[1]/div[1]/strong")
    TITLE_OF_PRODUCT = (By. XPATH, "//div[2]/h1")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-info p:nth-child(1)")
    BASKET_MESSAGE_PRODUCT_PRICE = (By.XPATH, "//div[1]/p/strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "div.product_main p.price_color")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")


class BasketPageLocators:
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
