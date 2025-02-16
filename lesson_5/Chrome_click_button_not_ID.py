from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Открываем страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Находим кнопку по CSS селектору и кликаем по ней
button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

# Ждем немного, чтобы увидеть результат
time.sleep(5)

# Закрываем браузер
driver.quit()
