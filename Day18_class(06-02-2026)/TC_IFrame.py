from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
#driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)
driver.get("https://letcode.in/frame")
time.sleep(5)

iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.NAME, "fname").send_keys("abhi")
driver.find_element(By.NAME, "lname").send_keys("ram")

insight = driver.find_element(By.XPATH, "//p[text()=' Insight ']").is_displayed()
print(insight)