from selenium import webdriver
import time

# 1. Open browser
driver = webdriver.Firefox()
driver.maximize_window()

# 2. Navigate to TutorialsNinja Home Page
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)
print("Home Page Title:", driver.title)
time.sleep(2)

# 3. Navigate to another page on the same site (Register page)
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(2)
print("Register Page Title:", driver.title)
time.sleep(2)

# 4. Use back()
driver.back()
time.sleep(2)
print("After Back - Title:", driver.title)
time.sleep(2)

# 5. Use forward()
driver.forward()
time.sleep(2)
print("After Forward - Title:", driver.title)
time.sleep(2)

# 6. Use refresh()
driver.refresh()
time.sleep(2)
print("After Refresh - Title:", driver.title)
time.sleep(2)

# 7. Close browser
driver.quit()
