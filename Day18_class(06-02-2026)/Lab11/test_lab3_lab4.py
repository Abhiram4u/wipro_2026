from desktop_page import DesktopPage


def test_lab3_lab4_flow(setup):
    driver = setup

    # Create Page Object
    desktop_page = DesktopPage(driver)

    # Step 1: Open Mac Page
    desktop_page.open_mac_page()

    # Step 2: Verify Heading (Lab4 Assertion)
    assert desktop_page.verify_mac_heading() == "Mac"
    print("Verified Mac heading")

    # Step 3: Sort Products
    desktop_page.sort_by_name_az()
    print("Sorted products by Name (A-Z)")

    # Step 4: Add to Cart
    desktop_page.click_add_to_cart()
    print("Product added to cart")

    # Step 5: Search for Monitors
    desktop_page.search_product("Monitors")
    print("Search initiated")

    # Step 6: Search with Description checkbox
    desktop_page.advanced_search_with_description()
    print("Advanced search completed")
