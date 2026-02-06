from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class DesktopPage:
    """
    Page Factory Style Page Object
    Contains locators + reusable actions
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators (Page Factory Style)
    desktops_menu = (By.LINK_TEXT, "Desktops")
    mac_option = (By.LINK_TEXT, "Mac (1)")
    page_heading = (By.CSS_SELECTOR, "h2")

    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_btn = (By.CSS_SELECTOR, ".button-group > button:nth-child(1)")

    search_box_top = (By.NAME, "search")
    search_icon = (By.CSS_SELECTOR, ".fa-search")

    search_input = (By.ID, "input-search")
    description_checkbox = (By.ID, "description")
    search_button = (By.ID, "button-search")

    # Page Actions
    def open_mac_page(self):
        self.wait.until(EC.element_to_be_clickable(self.desktops_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.mac_option)).click()

    def verify_mac_heading(self):
        heading = self.wait.until(EC.visibility_of_element_located(self.page_heading)).text
        return heading

    def sort_by_name_az(self):
        dropdown_element = self.wait.until(EC.element_to_be_clickable(self.sort_dropdown))
        select = Select(dropdown_element)
        select.select_by_visible_text("Name (A - Z)")

    def click_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn)).click()

    def search_product(self, product_name):
        self.wait.until(EC.element_to_be_clickable(self.search_box_top)).click()
        self.driver.find_element(*self.search_box_top).send_keys(product_name)

        self.wait.until(EC.element_to_be_clickable(self.search_icon)).click()

    def advanced_search_with_description(self):
        self.wait.until(EC.element_to_be_clickable(self.description_checkbox)).click()
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
