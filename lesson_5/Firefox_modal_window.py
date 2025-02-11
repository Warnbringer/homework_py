from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Создаем экземпляр веб-драйвера для Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу с модальным окном
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # Ждем 2 секунды, чтобы страница успела загрузиться
    time.sleep(2)

    # Находим кнопку закрытия модального окна по CSS селектору
    close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p")
    # Кликаем на кнопку закрытия
    close_button.click()

finally:
    # Ждем 2 секунды, чтобы увидеть результат перед закрытием браузера
    time.sleep(2)
    # Закрываем браузер
    driver.quit()
