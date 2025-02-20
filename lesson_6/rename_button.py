from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

# Переходим на сайт
driver.get("http://uitestingplayground.com/textinput")

# Указываем в поле ввода текст SkyPro
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# Жмем на синюю кнопку
button = driver.find_element(By.ID, "updatingButton")
button.click()

# Получаем текст кнопки и выводим в консоль
button_text = button.text
print(button_text)

sleep(4)

# Закрываем драйвер
driver.quit()
