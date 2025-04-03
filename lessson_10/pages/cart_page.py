from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver

    def proceed_to_checkout(self):
        """
        Переходит к оформлению заказа.
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Checkout']"))).click()
