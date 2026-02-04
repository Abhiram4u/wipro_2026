
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTc001():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tc001(self):
        expectedurl = "https://tutorialsninja.com/demo/index.php?route=account/register"
        self.driver.get(expectedurl)
        self.driver.set_window_size(1200, 800)
        time.sleep(2)



        # LOCATORS & INPUT ACTIONS


        # ID locator
        self.driver.find_element(By.ID, "input-firstname").send_keys("Abhi")
        time.sleep(2)


        # Name locator
        self.driver.find_element(By.NAME, "lastname").send_keys("Ram")
        time.sleep(2)

        # CSS Selector locator
        self.driver.find_element(By.CSS_SELECTOR, "#input-email").send_keys("abhiramvarma06o9@gmail.com")
        time.sleep(2)

        # XPath locator
        self.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys("8498809850")
        time.sleep(2)

        # Class Name locator
        inputs = self.driver.find_elements(By.CLASS_NAME, "form-control")
        inputs[5].send_keys("abhi@123")
        time.sleep(2)

        # ID locator
        self.driver.find_element(By.ID, "input-confirm").send_keys("abhi@123")
        time.sleep(2)

        # RADIO BUTTON & CHECKBOX
        self.driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
        time.sleep(2)


        # SUBMIT FORM
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        time.sleep(2)


        # VALIDATION MESSAGE


        success_text = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/h1"
        ).text
        assert success_text == "Your Account Has Been Created!"

        print("TEST PASSED: Account created successfully")
