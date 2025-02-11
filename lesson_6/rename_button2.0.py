from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Ожидаем, пока текст кнопки изменится, и получаем его
button_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

# Получаем текст кнопки и выводим в консоль
print("Текст кнопки:", button.text)

# Закрываем драйвер
driver.quit()
