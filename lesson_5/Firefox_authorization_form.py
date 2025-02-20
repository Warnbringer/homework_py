from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр веб-драйвера для Chrome
driver = webdriver.Firefox()

try:
    # Открываем страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Находим поле username и вводим значение
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("tomsmith")

    # Ждем немного, чтобы увидеть результат
    time.sleep(2)

    # Находим поле password и вводим значение
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Ждем немного, чтобы увидеть результат
    time.sleep(2)

    # Находим кнопку Login и нажимаем на нее
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Ждем немного, чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()
