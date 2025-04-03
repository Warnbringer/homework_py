import pytest
from selenium import webdriver
from pages.form_page import FormPage

url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.quit()

def test_form_submission(setup):
    driver = setup
    form_page = FormPage(driver)
    form_page.open()

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

    # Заполнение формы
    form_page.fill_form(form_data)

    # Нажатие кнопки Submit
    form_page.submit()

    # Проверка, что элемент с ошибкой Zip code присутствует в DOM
    zip_code_alert = form_page.get_zip_code_alert()

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
        field = form_page.get_field(field_name)
        # Проверка наличия класса alert-success
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_name} не подсвечено зеленым"
