import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
discount_product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', [
    f"{discount_product_link}/?promo=offer{x}"
    if x != 7 else pytest.param(f"{discount_product_link}/?promo=offer{x}", marks=pytest.mark.xfail)
    for x in range(10)
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_contains_correct_product_name()
    page.message_contains_correct_total_cost()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link, timeout=0)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_adding_product_is_not_presented()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_base_link, timeout=0)
    page.open()
    page.message_adding_product_is_not_presented()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_base_link, timeout=0)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_adding_product_has_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_base_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
