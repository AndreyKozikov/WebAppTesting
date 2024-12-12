import pytest
import yaml
import requests

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    username = config['username']
    password = config['password']
    url = config['url']

@pytest.fixture()
def coord_for_search():
    return "37.7891838", "-122.4033522"

@pytest.fixture()
def test_for_search():
    return "One Montgomery Tower"

@pytest.fixture(scope='session')
# Логинимся на сайт и получаем токен
def site_login():
    params = {
        'username': username,
        'password': password
    }
    response = requests.post(url + "gateway/login", data=params)
    if response.status_code != 200:
        raise Exception(f"Login failed {response.status_code} - {response.text}")
    token = response.json().get("token")
    return token

@pytest.fixture()
# Создаем сессию для выполнения запросов
def api_session(site_login):
    session = requests.Session()
    session.headers.update({"X-Auth-Token": site_login})  # Устанавливаем заголовок с токеном
    yield session
    session.close()

@pytest.fixture()
# Поиск чужого поста по заголовку
def seacrh_post_by_title():
    return "test title"

@pytest.fixture()
# Создание нового поста
def create_post(api_session):
    data = {
        "title": "Pytest test",
        "description": "Learning pytest",
        "content": "test content for testing API using pytest",
    }
    response = api_session.post(url + "api/posts", data=data)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception(f"Failed to create post: {response.status_code} - {response.text}")
    return data["description"]