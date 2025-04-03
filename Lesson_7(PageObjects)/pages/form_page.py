# pages/form_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, form_data):
        for field_name, value in form_data.items():
            field = WebDriverWait(self.driver, 4).until(
                EC.element_to_be_clickable((By.NAME, field_name))
            )
            field.clear()  # Очистка поля перед вводом
            field.send_keys(value)  # Ввод данных

    def submit(self):
        submit_button = WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button.btn.btn-outline-primary.mt-3"))
        )
        submit_button.click()

    def get_zip_code_alert(self):
        return WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, "zip-code"))
        )

    def get_field(self, field_name):
        return WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, field_name))
        )
