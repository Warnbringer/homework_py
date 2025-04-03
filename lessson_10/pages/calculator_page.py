from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_display = (By.CLASS_NAME, "screen")

    def set_delay(self, value):
        """
        Устанавливает задержку в поле ввода.

        :param value: str, значение задержки для ввода.
        """
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(value)

    def click_button(self, button):
        """
        Нажимает на указанную кнопку.

        :param button: tuple, локатор кнопки для нажатия.
        """
        button_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button)
        )
        button_element.click()

    def get_result(self):
        """
        Получает результат вычисления.

        :return: str, текст результата.
        """
        # Ожидание, пока результат не станет видимым
        result_element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.result_display)
        )
        return result_element.text.strip()
