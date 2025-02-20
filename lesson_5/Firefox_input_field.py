from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр веб-драйвера для Chrome
driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Находим поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Вводим текст 1000
    input_field.send_keys("1000")
    time.sleep(2)  # Задержка для наглядности

    # Очищаем поле
    input_field.clear()
    time.sleep(2)  # Задержка для наглядности

    # Вводим текст 999
    input_field.send_keys("999")
    time.sleep(2)  # Задержка для наглядности

finally:
    # Закрываем браузер
    driver.quit()
