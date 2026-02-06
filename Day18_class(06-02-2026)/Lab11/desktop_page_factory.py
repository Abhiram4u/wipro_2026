from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DesktopPageFactory:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    # PageFactory Locators (@property)


    @property
    def desktops_menu(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")

    @property
    def mac_option(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")

    @property
    def heading_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h2")

    @property
    def sort_dropdown(self):
        return self.driver.find_element(By.ID, "input-sort")

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button-group > button:nth-child(1)")

    @property
    def search_box(self):
        return self.driver.find_element(By.NAME, "search")

    @property
    def search_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".fa-search")

    @property
    def description_checkbox(self):
        return self.driver.find_element(By.ID, "description")

    @property
    def search_button(self):
        return self.driver.find_element(By.ID, "button-search")


    # Page Actions (Methods)


    def click_desktops(self):
        self.desktops_menu.click()

    def click_mac(self):
        self.mac_option.click()

    def verify_mac_heading(self):
        return self.heading_text.text

    def sort_name_az(self):
        dropdown = Select(self.sort_dropdown)
        dropdown.select_by_visible_text("Name (A - Z)")

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def search_product(self, product):
        self.search_box.clear()
        self.search_box.send_keys(product)
        self.search_icon.click()

    def enable_description_search(self):
        self.description_checkbox.click()

    def click_search_button(self):
        self.search_button.click()
