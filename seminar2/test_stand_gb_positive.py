import time
from testoperations import TestOperations
import yaml

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    browser_name = config['browser'].lower()
    username = config['username']
    password = config['password']
    url = config['url']

def test_login(browser, success_login):
    test_page = TestOperations(browser)
    test_page.get_web_page()
    test_page.enter_login(username)
    test_page.enter_password(password)
    test_page.click_login_button()
    greeting = test_page.check_success_login()
    assert greeting == success_login


def test_new_post_add(browser, new_post_create):
    test_page = TestOperations(browser)
    test_page.click_create_post_button()
    time.sleep(2)
    test_page.enter_title_post(new_post_create[0])
    test_page.enter_desc_post(new_post_create[1])
    test_page.enter_content_post(new_post_create[2])
    test_page.click_save_post_button()
    time.sleep(8)
    assert test_page.check_title_after_create() == new_post_create[0]