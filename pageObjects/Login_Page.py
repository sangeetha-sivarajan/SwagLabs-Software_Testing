from selenium.webdriver.common.by import By

from Util_files.browser_utils import Browser_utils_file
from pageObjects.Products_Page import productpage


class loginPage(Browser_utils_file):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_login=(By.ID,"user-name")
        self.password_login = (By.ID,"password")
        self.login_button = (By.ID,"login-button")


    def login1(self,UserName,PassWord):
        self.driver.find_element(*self.username_login).send_keys(UserName)
        self.driver.find_element(*self.password_login).send_keys(PassWord)
        self.driver.find_element(*self.login_button).click()
        try:
            error_element = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
            if error_element.is_displayed():
                return {"status": "fail", "error_message": error_element.text}
        except:
            pass

        # Successful login
        shop_products = productpage(self.driver)
        return {"status": "pass", "page": shop_products}

