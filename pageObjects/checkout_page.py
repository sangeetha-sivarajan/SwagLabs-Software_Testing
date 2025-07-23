import time

from selenium.webdriver.common.by import By

from Util_files.browser_utils import Browser_utils_file


class checkout_Page(Browser_utils_file):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button= (By.CLASS_NAME,"checkout_button")
        self.info_submit = (By.CSS_SELECTOR,".btn_primary.cart_button")
        self.finish = (By.CLASS_NAME,"btn_action")
        self.sidebar_menu = (By.CLASS_NAME,"bm-burger-button")
        self.logout_option = (By.ID,"logout_sidebar_link")
        self.success_message = (By.CSS_SELECTOR,".complete-text")



    def your_cart(self):
        self.driver.find_element(*self.checkout_button).click()

    def your_information(self,FirstName,LastName,PostalCode):
        self.driver.find_element(By.ID,"first-name").send_keys(FirstName)
        self.driver.find_element(By.ID,"last-name").send_keys(LastName)
        self.driver.find_element(By.ID,"postal-code").send_keys(PostalCode)
        self.driver.find_element(*self.info_submit).click()

    def checkout_overview(self):
        self.driver.find_element(*self.finish).click()

    def validation(self):
        dispatch_detail = self.driver.find_element(*self.success_message).text
        assert "Your order has been dispatched" in dispatch_detail
        print(dispatch_detail)


    def logout(self):
        self.driver.find_element(*self.sidebar_menu).click()
        self.driver.find_element(*self.logout_option).click()
        time.sleep(2)













