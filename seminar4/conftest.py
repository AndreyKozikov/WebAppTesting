import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    browser_name = config['browser'].lower()
    name = config["username"]
    password = config["password"]
    url = config["url"]



@pytest.fixture(scope='session')
def browser():
    if browser_name == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture()
def new_post_create():
    title = "Selenium"
    description = "Selenium test"
    content = "Post created via Selenium."
    return title, description, content

@pytest.fixture()
def success_login():
    return f"Hello, {name}"

@pytest.fixture()
def login_fail():
    return "401"

@pytest.fixture()
def contact_us_data():
    your_name = "test"
    email = "test@email.gb"
    content = "test content"
    return your_name, email, content

@pytest.fixture()
def contact_us_header_text():
    text = "Contact us!"
    return text

@pytest.fixture()
def alert_text():
    return "Form successfully submitted"

@pytest.fixture(scope='session')
def new_post():
    return {
        "title": "Pytest test",
        "description": "Learning pytest",
        "content": "test content for testing API using pytest"
    }

@pytest.fixture()
# Создаем сессию для выполнения запросов
def api_session():
    params = {
        'username': name,
        'password': password
    }
    response = requests.post(url + "gateway/login", data=params)
    if response.status_code != 200:
        raise Exception(f"Login failed {response.status_code} - {response.text}")
    token = response.json().get("token")
    session = requests.Session()
    session.headers.update({"X-Auth-Token": token})  # Устанавливаем заголовок с токеном
    yield session
    session.close()

@pytest.fixture()
# Поиск чужого поста по заголовку
def search_post_by_title():
    return "test title"

