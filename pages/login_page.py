
from locators.login_locators import LoginLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.enter_text(LoginLocators.USERNAME, username)
        self.enter_text(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)
