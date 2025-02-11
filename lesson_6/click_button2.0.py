from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("http://uitestingplayground.com/ajax")

# Ждем появления синей кнопки и кликаем на неё
button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )
button.click()

# Ждем появления зеленой плашки и получаем текст
green_message = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)
text = green_message.text

# Выводим текст в консоль
print(text)

# Закрываем драйвер
driver.quit()
