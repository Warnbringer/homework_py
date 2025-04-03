from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_ids):
        for product_id in product_ids:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.ID, product_id))).click()
