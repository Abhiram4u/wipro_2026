from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    # driver = webdriver.Firefox()
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginbutton = (By.XPATH, "//button[@type='submit']")

    def enterusername(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def enterpassword(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def loginbutton(self):
        self.driver.find_element(*self.loginbutton).click()