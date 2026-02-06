from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):

    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    dashboard_heading = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, username, password):
        self.enter_text(self.username_input, username)
        self.enter_text(self.password_input, password)
        self.click(self.login_button)

    def is_dashboard_visible(self):
        return self.get_text(self.dashboard_heading) == "Dashboard"
