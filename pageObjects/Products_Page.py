import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Util_files.browser_utils import Browser_utils_file
from pageObjects.checkout_page import checkout_Page


class productpage(Browser_utils_file):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.sortproducts = (By.CSS_SELECTOR,".product_sort_container")
        self.productname = (By.XPATH,"div[2]/a/div")
        self.products_list = (By.XPATH,"//div[@class='inventory_item']")
        self.addtocartbutton = (By.CSS_SELECTOR,".btn_primary.btn_inventory")
        self.backbutton = (By.CSS_SELECTOR,".inventory_details_back_button")
        self.cartIcon_click = (By.CLASS_NAME,"shopping_cart_link")

# sorting the products
    def sorting(self):
        sort_dropdown = Select(self.driver.find_element(*self.sortproducts ))
        sort_dropdown.select_by_index(1)
        time.sleep(2)
        sort_dropdown.select_by_index(2)
# adding the product  to cart
    def add_cart(self):
        products_list =self.driver.find_elements(*self.products_list)
        for products in  products_list:
            products_name = products.find_element(*self.productname).text
            if products_name == "Sauce Labs Bike Light":
                products.find_element(By.XPATH,"div[2]/a").click()
                time.sleep(5)

                self.driver.find_element(*self.addtocartbutton).click()
                self.driver.find_element(*self.backbutton).click()
        for products_cost in products_list:
            price_text = products_cost.find_element(By.XPATH,"div[3]/div").text
            product_price = float(price_text.replace('$', '').strip())
            if product_price <= 20.00:
                self.driver.find_element(*self.addtocartbutton).click()
        time.sleep(5)

    def products_cart(self):
        self.driver.find_element(*self.cartIcon_click).click()
        time.sleep(2)
        checkout_product = checkout_Page(self.driver)
        return checkout_product






                









































