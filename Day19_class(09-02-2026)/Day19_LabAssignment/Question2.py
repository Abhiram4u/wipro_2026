from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Selenium Grid Hub URL
GRID_URL = "http://172.20.10.3:4444/wd/hub"

# Website to test
TEST_URL = "https://www.google.com"

# Browsers list
browsers = ["chrome", "firefox", "edge"]

for browser in browsers:
    print("---------------------------------")
    print(f"Running Test on {browser.upper()}")



    # Set browser options
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        print("Unsupported browser!")
        continue

    # Connect to Selenium Grid
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    # Print Browser + Platform Info
    caps = driver.capabilities
    print("Browser Name:", caps.get("browserName"))
    print("Platform:", caps.get("platformName"))

    # Open Website
    driver.get(TEST_URL)

    # Verify Title
    actual_title = driver.title
    print("Page Title:", actual_title)

    if "Google" in actual_title:
        print("Title Verified Successfully!")
    else:
        print("Title Mismatch!")

    driver.quit()

print("\nCross Browser Testing Completed!")
