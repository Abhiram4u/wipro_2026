from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# 1: Launch Browser

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 2: Open LetCode Frame Page

driver.get("https://letcode.in/frame")

print("Parent Page Title:", driver.title)


# 3: Switch to First iFrame

wait.until(
    EC.frame_to_be_available_and_switch_to_it((By.NAME, "firstFr"))
)

print("Switched to first iframe")


#4: Enter Text in Input Field Inside iFrame

first_name = wait.until(
    EC.visibility_of_element_located((By.NAME, "fname"))
)
first_name.send_keys("Abhiramakrishna")

last_name = driver.find_element(By.NAME, "lname")
last_name.send_keys("M")
time.sleep(2)

print("Entered First Name and Last Name inside iframe")

#5: Switch Back to Main Page

driver.switch_to.default_content()
time.sleep(2)
print("witched back to main content")

# 6: Open New Browser Tab

driver.execute_script("window.open('https://example.com', '_blank');")
time.sleep(2)

# Wait until 2 windows are opened
wait.until(lambda d: len(d.window_handles) == 2)

windows = driver.window_handles
parent_window = windows[0]
child_window = windows[1]

print("\nTotal Windows Opened:", len(windows))


#7: Switch Between Windows & Print Titles

driver.switch_to.window(parent_window)
time.sleep(2)
print("Parent Window Title:", driver.title)

driver.switch_to.window(child_window)
time.sleep(2)
print("Child Window Title:", driver.title)

# Step 8: Close Child Window

driver.close()
print("Child window closed")


# Step 9: Switch Back to Parent Window

driver.switch_to.window(parent_window)
time.sleep(2)
print("Returned to Parent Window:", driver.title)


# Quit Browser

driver.quit()
