import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()

def test_slow_calculator(setup):
    driver = setup
    calculator = CalculatorPage(driver)

    # Установка задержки
    calculator.set_delay("45")

    # Нажатие кнопок
    calculator.click_button(calculator.button_7)
    calculator.click_button(calculator.button_plus)
    calculator.click_button(calculator.button_8)
    calculator.click_button(calculator.button_equals)

    # Ожидание результата с помощью WebDriverWait
    result = WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Получаем результат
    result_value = calculator.get_result()

    # Проверка результата
    assert result_value == "15", f"Ожидалось '15', но получено '{result_value}'"
