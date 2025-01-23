from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Открываем браузер и страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

# Кликаем на синюю кнопку, используя CSS-класс
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

sleep(5)

driver.quit()
