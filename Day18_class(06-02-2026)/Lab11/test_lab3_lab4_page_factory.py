from desktop_page_factory import DesktopPageFactory
import time


def test_lab3_lab4_flow(setup):

    driver = setup
    desktop_page = DesktopPageFactory(driver)

    # Step 1: Click Desktops
    time.sleep(2)
    desktop_page.click_desktops()

    # Step 2: Click Mac (1)
    time.sleep(2)
    desktop_page.click_mac()

    # Step 3: Verify Heading = Mac (Lab4 Assertion)
    time.sleep(2)
    assert desktop_page.verify_mac_heading() == "Mac"
    print("Heading Verified: Mac")

    # Step 4: Sort Dropdown → Name (A-Z)
    time.sleep(2)
    desktop_page.sort_name_az()
    print("Sorted by Name (A-Z)")

    # Step 5: Add Product to Cart
    time.sleep(2)
    desktop_page.click_add_to_cart()
    print("Product Added to Cart")

    # Step 6: Search for Monitors
    time.sleep(2)
    desktop_page.search_product("Monitors")
    print("Search Done")

    # Step 7: Enable Description Checkbox
    time.sleep(2)
    desktop_page.enable_description_search()

    # Step 8: Click Search Button
    time.sleep(2)
    desktop_page.click_search_button()
    print("Advanced Search Completed")
