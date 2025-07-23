import json
import pytest
from selenium.webdriver.common.by import By

from Util_files.logger import get_logger
from pageObjects.Login_Page import loginPage

logger = get_logger()

test_data_path = "C:\\Users\\HP\PycharmProjects\\E-commerceDemotest\\test_Data\\test_swaglabs.json"
with open(test_data_path) as file1:
    test_data = json.load(file1)
    test_list = test_data["data"]


@pytest.mark.parametrize("testlist_items",test_list)
def test_SwagLabs(browserInstance,testlist_items):
    driver = browserInstance
    login_credential= loginPage(driver)
    print(login_credential.getTitle())
    logger.info("===== Starting test for user: %s =====", testlist_items["UserName"])
    logger.debug("Page Title: %s", login_credential.getTitle())
    result = login_credential.login1(testlist_items["UserName"], testlist_items["PassWord"])
    if result["status"] == "fail":
        screenshot_path = f"screenshots/{testlist_items['UserName']}_invalid_login.png"
        driver.save_screenshot(screenshot_path)
        print(f"Manual screenshot saved: {screenshot_path}")
        logger.warning("Login failed. Screenshot saved: %s", screenshot_path)
        logger.error("Login failed error message: %s", result["error_message"])
        # This is expected behavior for wrong credentials
        assert "Username and password do not match" in result["error_message"] or "Epic sadface" in result[
            "error_message"]
        print("Login failed as expected. Error message:", result["error_message"])
        return  # Skip the rest of the test if login failed

        # Login successful — continue with product and checkout steps
    shop_products = result["page"]
    print(shop_products.getTitle())
    logger.info("Login successful for user: %s", testlist_items["UserName"])
    logger.debug("Product Page Title: %s", shop_products.getTitle())
    shop_products.sorting()
    logger.info("Sorted products.")
    shop_products.add_cart()
    logger.info("Added products to cart.")
    checkout_product= shop_products.products_cart()
    logger.debug("Cart Page Title: %s", checkout_product.getTitle())
    print(checkout_product.getTitle())
    checkout_product.your_cart()
    logger.info("Navigated to cart.")
    checkout_product.your_information(testlist_items["FirstName"],testlist_items["LastName"],testlist_items["PostalCode"])
    logger.info("Filled user information.")
    # Check for error on missing checkout fields (e.g., PostalCode)
    try:
        error_element = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        if error_element.is_displayed():
            screenshot_path = f"screenshots/{testlist_items['FirstName']}_invalid_login.png"
            driver.save_screenshot(screenshot_path)
            print(f"Manual screenshot saved: {screenshot_path}")
            logger.warning("Checkout error occurred. Screenshot saved: %s", screenshot_path)
            logger.error("Checkout validation message: %s", error_element.text)
            assert "Error" in error_element.text
            print("Checkout validation failed as expected:", error_element.text)
            return  # Do not continue checkout steps
    except Exception as e:
        logger.debug("No checkout error message found. Proceeding...")
    # If no error — complete checkout
    checkout_product.checkout_overview()
    logger.info("Viewed checkout overview.")
    checkout_product.validation()
    logger.info("Validated order summary.")
    checkout_product.logout()
    logger.info("Logged out successfully.")
    logger.info("===== Test completed for user: %s =====\n", testlist_items["UserName"])





