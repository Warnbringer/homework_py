from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver"
               "-java/slow-calculator.html")

    try:
        # Ввод значения в поле delay
        delay_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажатие на кнопки
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
        ).click()

        # Ожидание результата
        result_element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "screen"))
        )

        # Ожидание, пока текст не изменится на "15"
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Проверка результата
        result = result_element.text.strip()  # Получаем текст результата
        assert result == "15", f"Ожидалось '15', но получено '{result}'"

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    finally:
        driver.quit()
