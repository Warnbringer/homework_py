# pages/form_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        """
        Инициализация страницы формы.

        :param driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        """
        Открывает страницу формы.
        """
        self.driver.get(self.url)

    def fill_form(self, form_data):
        """
        Заполняет форму данными из словаря.

        :param form_data: dict, данные для заполнения формы.
        """
        for field_name, value in form_data.items():
            field = WebDriverWait(self.driver, 4).until(
                EC.element_to_be_clickable((By.NAME, field_name))
            )
            field.clear()  # Очистка поля перед вводом
            field.send_keys(value)  # Ввод данных

    def submit(self):
        """
        Отправляет заполненную форму.
        """
        submit_button = WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button.btn.btn-outline-primary.mt-3"))
        )
        submit_button.click()

    def get_zip_code_alert(self):
        """
        Получает текст предупреждения о почтовом коде.

        :return: str, текст предупреждения.
        """
        return WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, "zip-code"))
        )

    def get_field(self, field_name):
        """
        Получает значение указанного поля.

        :param field_name: str, имя поля для получения значения.
        :return: str, значение поля.
        """
        return WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, field_name))
        )
