from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_shopping_cart():
    # Открываем сайт магазина
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Авторизуемся как пользователь standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce" + Keys.RETURN)

    # Добавляем товары в корзину
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    # Переходим в корзину
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='shopping_cart_link']"))).click()

    # Нажимаем Checkout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Checkout']"))).click()

    # Заполняем форму своими данными
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.ID, "first-name"))).send_keys("Рома")
    driver.find_element(By.ID, "last-name").send_keys("Роман")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Читаем итоговую стоимость
    total = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@class='summary_total_label']"))).text
    print(total)  # Для отладки, можно убрать в финальной версии

    # Закрываем браузер
    driver.quit()

    # Проверяем, что итоговая сумма равна $58.29
    assert total == "Total: $58.29"

# Запуск теста
if __name__ == "__main__":
    test_shopping_cart()
