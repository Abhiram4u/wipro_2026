from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# -----------------------------
# Step 1: Define Variables First
# -----------------------------

base_url = "https://tutorialsninja.com/demo/"
expected_title = "Your Store"
expected_heading = "Register Account"
expected_warning_message = "Warning: You must agree to the Privacy Policy!"

# -----------------------------
# Step 2: Launch Firefox Browser
# -----------------------------

driver = webdriver.Firefox()
driver.maximize_window()

# -----------------------------
# Step 3: Open Application URL
# -----------------------------

driver.get(base_url)
time.sleep(2)

# -----------------------------
# Step 4: Verify Title of Page
# -----------------------------

actual_title = driver.title

if actual_title == expected_title:
    print("Title Verified Successfully:", actual_title)
else:
    print("Title Mismatch!")
    print("Expected:", expected_title)
    print("Actual:", actual_title)

# -----------------------------
# Step 5: Click on My Account Dropdown
# -----------------------------

my_account_dropdown = driver.find_element(By.XPATH, "//span[text()='My Account']")
my_account_dropdown.click()
time.sleep(2)

# -----------------------------
# Step 6: Select Register Option
# -----------------------------

register_option = driver.find_element(By.LINK_TEXT, "Register")
register_option.click()
time.sleep(2)

# -----------------------------
# Step 7: Verify Register Account Heading
# -----------------------------

heading_element = driver.find_element(By.XPATH, "/html/body/div/div/div/h1")
actual_heading = heading_element.text

if actual_heading == expected_heading:
    print(" Heading Verified Successfully:", actual_heading)
else:
    print("Heading Mismatch!")
    print("Expected:", expected_heading)
    print("Actual:", actual_heading)

# -----------------------------
# Step 8: Click Continue Button Without Filling Form
# -----------------------------

continue_button = driver.find_element(By.XPATH, "//input[@value='Continue']")
continue_button.click()
time.sleep(2)

# -----------------------------
# Step 9: Verify Warning Message
# -----------------------------

warning_element = driver.find_element(
    By.XPATH, "//div[contains(@class,'alert-danger')]"
)

actual_warning = warning_element.text

if expected_warning_message in actual_warning:
    print(" Warning Message Verified Successfully!")
    print("Message:", actual_warning)
else:
    print(" Warning Message Not Matching!")
    print("Expected:", expected_warning_message)
    print("Actual:", actual_warning)

# -----------------------------
# Step 10: Close Browser
# -----------------------------

driver.quit()
print(" Browser Closed Successfully")
