import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2/projects"
AUTH_COMPANIES_URL = "https://ru.yougile.com/api-v2/auth/companies"
AUTH_KEYS_URL = "https://ru.yougile.com/api-v2/auth/keys"
TOKEN = None
COMPANY_ID = None


# Получение списка компаний и токена
def get_auth_token():
    global TOKEN, COMPANY_ID
    # Получение списка компаний
    auth_response = requests.post(AUTH_COMPANIES_URL, json={
        "login": "warnbringer@gmail.com",
        "password": "!Lost4815162342"
    })

    if auth_response.status_code == 200:
        companies = auth_response.json()
        print("Список компаний:", companies)  # Отладочная информация
        if ('content' in companies and isinstance(companies['content'],
                                                  list) and
                companies['content']):
            COMPANY_ID = companies['content'][0]['id']
        else:
            raise Exception("Список компаний пуст или не является списком")
    else:
        raise Exception(f"Не удалось получить список компаний: "
                        f"{auth_response.status_code} - {auth_response.text}")

    # Получение ключа
    key_response = requests.post(AUTH_KEYS_URL, json={
        "login": "warnbringer@gmail.com",
        "password": "!Lost4815162342",
        "companyId": COMPANY_ID
    })

    if key_response.status_code == 201:  # Изменено на 201
        TOKEN = key_response.json().get("key")  # Изменено на "key"
    else:
        raise Exception(f"Не удалось получить токен авторизации: "
                        f"{key_response.status_code} - {key_response.text}")


# Позитивные тесты
def test_create_project():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(BASE_URL, json={"title": "Кабинет бобра"},
                             headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()


def test_update_project():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    # Предположим, что проект с ID существует
    project_id = "31b80ef3-6d98-4082-ad34-d2d70cc605bc"

    # Обновляем проект
    response = requests.put(
        f"{BASE_URL}/{project_id}",
        json={
            "deleted": True,
            "title": "Кабинет бобрика",
            "users": {
                "744b49e8-b01c-4012-9789-5f5ef05f006c": "worker"
            }
        },
        headers=headers
    )

    # Проверяем статус-код
    assert response.status_code == 200

    # Получаем обновленный проект
    get_response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
    assert get_response.status_code == 200

    # Проверяем, что title обновился
    get_response_data = get_response.json()
    assert get_response_data["title"] == "Кабинет бобрика", \
        "Название проекта не обновилось"


def test_get_project():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    project_id = "31b80ef3-6d98-4082-ad34-d2d70cc605bc"
    response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
    assert response.status_code == 200
    assert "title" in response.json()


# Негативные тесты
def test_create_project_without_title():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(BASE_URL, json={}, headers=headers)
    assert response.status_code == 400  # Ожидаем ошибку 400 Bad Request


def test_update_nonexistent_project():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(f"{BASE_URL}/9999", json={
        "deleted": True,
        "title": "Nonexistent Project",
        "users": {}
    }, headers=headers)
    assert response.status_code == 404  # Ожидаем ошибку 404 Not Found


def test_get_nonexistent_project():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(f"{BASE_URL}/9999", headers=headers)
    assert response.status_code == 404  # Ожидаем ошибку 404 Not Found


# Вызов функции для получения токена перед запуском тестов
get_auth_token()
