from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        """
        Заполняет форму оформления заказа.

        :param first_name: str, имя покупателя.
        :param last_name: str, фамилия покупателя.
        :param postal_code: str, почтовый код.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def get_total(self):
        """
        Получает общую сумму заказа.

        :return: str, текст общей суммы.
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='summary_total_label']"))).text
