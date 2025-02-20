from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_shopping_cart():
    # Открываем сайт магазина
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Создаем объекты страниц
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Авторизуемся как пользователь standard_user
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    products_page.add_to_cart([
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ])

    # Переходим в корзину
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

    # Нажимаем Checkout
    cart_page.proceed_to_checkout()

    # Заполняем форму своими данными
    checkout_page.fill_form("Рома", "Роман", "12345")

    # Читаем итоговую стоимость
    total = checkout_page.get_total()
    print(total)  # Для отладки, можно убрать в финальной версии

    # Закрываем браузер
    driver.quit()

    # Проверяем, что итоговая сумма равна $58.29
    assert total == "Total: $58.29"

# Запуск теста
if __name__ == "__main__":
    test_shopping_cart()
