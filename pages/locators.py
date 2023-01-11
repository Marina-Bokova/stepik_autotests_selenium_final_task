from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")  # //a[contains(text(), 'View basket')]


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    AVAILABILITY = (By.CSS_SELECTOR, ".availability")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    MESSAGE_ADDING = (By.XPATH, "//div[contains(@class, 'alertinner') and contains(string(), 'has been')]")
    MESSAGE_PRODUCT_NAME = (By.XPATH, f"{MESSAGE_ADDING[1]}/strong")
    MESSAGE_YOUR_BASKET = (By.XPATH, "//div[contains(@class, 'alertinner') and contains(string(), 'total is now')]")
    MESSAGE_YOUR_BASKET_TOTAL = (By.XPATH, f"{MESSAGE_YOUR_BASKET[1]}/p/strong")


class BasketPageLocators:
    NAME_PAGE = (By.CSS_SELECTOR, ".page-header h1")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.XPATH, '//p[contains(text(), "Your basket is empty")]')
