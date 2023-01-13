from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        url_page = self.browser.current_url
        assert "login" in url_page, \
            "Failed to go to login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), \
            "Register form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password, confirm_password=None):
        if confirm_password is None:
            confirm_password = password
        self.should_be_register_form()
        element_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        element_email.send_keys(email)
        element_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        element_password.send_keys(password)
        element_repeat_password = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD_FIELD)
        element_repeat_password.send_keys(confirm_password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def successful_register_new_user(self, email, password, confirm_password=None):
        self.register_new_user(email, password, confirm_password)
        assert self.is_element_present(*LoginPageLocators.SUCCESSFUL_REGISTRATION_MESSAGE), \
            "New user registration failed"
