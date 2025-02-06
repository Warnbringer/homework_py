from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # Ждем появления синей кнопки и кликаем на неё
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
    button.click()

    # Ждем появления зеленой плашки и получаем текст
    green_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "content"))
    )
    text = green_message.text

    # Выводим текст в консоль
    print(text)

    # если меньше 20 сек, то плашка не успевает появиться
    sleep(20)

finally:
    # Закрываем драйвер
    driver.quit()
