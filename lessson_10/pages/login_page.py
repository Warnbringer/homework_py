from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        """
        Инициализация страницы входа.

        :param driver: WebDriver, используемый для взаимодействия с браузером.
        """
        self.driver = driver

    def login(self, username, password):
        """
        Выполняет вход в систему.

        :param username: str, имя пользователя.
        :param password: str, пароль.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)
