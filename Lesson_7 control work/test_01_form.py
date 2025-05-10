from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest


driver_path = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()


def test_form_submission(setup):
    driver = setup

    # Данные для заполнения формы
    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",  # Оставляем пустым
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Ожидание появления элементов и заполнение формы
    for field_name, value in form_data.items():
        field = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.NAME, field_name))
        )
        field.clear()  # Очистка поля перед вводом
        field.send_keys(value)  # Ввод данных

    # Нажатие кнопки Submit
    submit_button = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "button.btn.btn-outline-primary.mt-3"))
    )
    submit_button.click()

    # Проверка, что элемент с ошибкой Zip code присутствует в DOM
    zip_code_alert = WebDriverWait(driver, 4).until(
        EC.visibility_of_element_located((By.ID, "zip-code"))
    )

    # Проверка, что текст ошибки отображается
    assert "N/A" in zip_code_alert.text, \
        "Ошибка не отображается для поля Zip code"

    # Проверка, что элемент имеет класс alert-danger
    assert "alert-danger" in zip_code_alert.get_attribute("class"), \
        "Поле Zip code не подсвечено красным"

    # Проверка, что остальные поля подсвечены зеленым
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_name in fields:
        try:
            field = WebDriverWait(driver, 4).until(
                EC.visibility_of_element_located((By.ID, field_name))
            )
            # Проверка наличия класса alert-success
            assert "alert-success" in field.get_attribute("class"), \
                f"Поле {field_name} не подсвечено зеленым"
        except TimeoutException:
            assert False, f"Поле {field_name} не найдено на странице"
        except Exception as e:
            assert False, (f"Произошла ошибка при проверке "
                           f"поля {field_name}: {str(e)}")
