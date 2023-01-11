from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def opened_page_is_basket(self):
        assert "Basket" in self.browser.find_element(*BasketPageLocators.NAME_PAGE).text, \
            "Opened page isn't basket"

    def basket_has_products(self):
        assert len(self.browser.find_elements(*BasketPageLocators.PRODUCTS_IN_BASKET)) != 0, "The basket is empty"

    def basket_has_not_products(self):
        assert len(
            self.browser.find_elements(*BasketPageLocators.PRODUCTS_IN_BASKET)) == 0, "The basket isn't empty"

    def message_is_present_in_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "The basket isn't empty"

    def message_is_not_present_in_no_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "The basket is empty"
