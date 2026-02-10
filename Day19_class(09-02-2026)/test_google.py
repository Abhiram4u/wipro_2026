import pytest
from driverfactory import getdriver

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_googletitle(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()


@pytest.mark.parametrize("browser", ["chrome","edge"])
def test_googlesearch(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com")

    searchbox = driver.find_element("name", "q")
    searchbox.send_keys("selenium grid")
    searchbox.submit()

    assert "selenium" in driver.title.lower()
    driver.quit()
