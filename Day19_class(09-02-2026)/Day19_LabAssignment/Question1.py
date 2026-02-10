from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


# Step 1: Launch Browser

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# 1. Implicit Wait Example

# Applies globally for all elements
driver.implicitly_wait(10)
print("Implicit wait applied (10 seconds)")

# Click Button to Enable Input Field

button = driver.find_element(By.XPATH, "//button[text()='Enable']")
button.click()


# 2. Explicit Wait Example

# Wait until input box becomes clickable
explicit_wait = WebDriverWait(driver, 10)

input_box = explicit_wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
)

print("Explicit Wait: Input box is now clickable!")


# 3. Fluent Wait Example
# Fluent wait = explicit wait + polling interval + ignored exceptions

fluent_wait = WebDriverWait(driver, 15, poll_frequency=2,
                            ignored_exceptions=[NoSuchElementException])

element = fluent_wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
)

print("Fluent Wait: Element is available for interaction!")


# Interact with Element
element.send_keys("Selenium Waits Example")
print("Successfully typed into the input box!")

# Close Browser
time.sleep(3)
driver.quit()
