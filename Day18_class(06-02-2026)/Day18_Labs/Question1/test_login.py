from login_page import LoginPage
from config import Config


def test_valid_login(setup):

    driver = setup

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    assert Config.DASHBOARD_URL in driver.current_url

    assert login_page.is_dashboard_visible()

    print("\n Test Passed: Login Successful & Dashboard Verified!")
