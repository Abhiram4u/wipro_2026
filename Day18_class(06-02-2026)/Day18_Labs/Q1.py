import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Base Page (Reusable Methods)

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text



# Login Page (POM Class)

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


# Pytest Setup Fixture
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver
    driver.quit()


# Test Case
def test_valid_login(setup):
    driver = setup

    login_page = LoginPage(driver)

    # Perform Login
    login_page.login("Admin", "admin123")

    # Validate Dashboard
    assert login_page.is_dashboard_visible()

    print("\nTest Passed: Login Successful!")
