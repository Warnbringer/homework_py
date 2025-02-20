from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Настройка драйвера
driver = webdriver.Chrome()

# Открытие страницы
driver.get("http://uitestingplayground.com/dynamicid")

# Клик на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

sleep(5)

driver.quit()

