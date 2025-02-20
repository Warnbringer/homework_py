from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем появления синей кнопки и кликаем на неё
image = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.TAG_NAME, "img"))
    )

# Ждем появления зеленой плашки и получаем текст
src = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "award"))
)
# Находим на странице элементы с тэгом img
images = driver.find_elements(By.TAG_NAME, "img")

# Выводим текст в консоль
if len(images) >= 3:
    third_image_src = images[3].get_attribute("src")
    print("Значение атрибута src у 3-й картинки:", third_image_src)
else:
    print("Недостаточно изображений на странице.")

# Закрываем драйвер
driver.quit()

# Интересно, почему в 27 строке значение картинки = images[3],
# ведь в питоне начинаем считать с 0,1,2, и, по-хорошему,
# должно быть 2 у третьей картинки
