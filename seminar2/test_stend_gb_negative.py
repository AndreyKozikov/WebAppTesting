import time
from testoperations import TestOperations
import yaml

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    browser_name = config['browser'].lower()
    username = config['username']
    password = config['password']
    url = config['url']

def test_login(browser, login_fail):
    test_page = TestOperations(browser)
    test_page.get_web_page()
    test_page.enter_login(username)
    test_page.enter_password(password)
    test_page.click_login_button()
    err = test_page.get_error_message()
    assert err == login_fail