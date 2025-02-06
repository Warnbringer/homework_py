from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

# Переходим на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
           )

# Ждем загрузки всех картинок
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)
# a few moments later...
sleep(12)

# Получаем значение атрибута src у 3-й картинки
images = driver.find_elements(By.TAG_NAME, "img")
third_image_src = images[3].get_attribute("src")

sleep(4)

# Выводим значение в консоль
print(third_image_src)

# Закрываем драйвер
driver.quit()
