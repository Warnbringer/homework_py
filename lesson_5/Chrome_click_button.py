from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Настройка веб-драйвера
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Клик на кнопку "Add Element" пять раз
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

# Список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print("Размер списка 'Delete':", len(delete_buttons))

sleep(5)

driver.quit()
