import time


from testoperations import OperationsHelper
import yaml

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)
    username = config['username']
    password = config['password']
    url = config['url']

def test_invalid_login(browser, login_fail):
    test_page = OperationsHelper(browser)
    test_page.get_web_page(url)
    test_page.enter_login(login_fail[0])
    test_page.enter_password(login_fail[1])
    test_page.click_login_button(False)
    err = test_page.get_error_message()
    assert err == login_fail

def test_login(browser, success_login):
    test_page = OperationsHelper(browser)
    test_page.get_web_page(url)
    test_page.enter_login(username)
    test_page.enter_password(password)
    test_page.click_login_button(True)
    greeting = test_page.check_success_login()
    assert greeting == success_login


def test_new_post_add(browser, new_post_create):
    test_page = OperationsHelper(browser)
    test_page.click_create_post_button()
    time.sleep(2)
    test_page.enter_title_post(new_post_create[0])
    test_page.enter_desc_post(new_post_create[1])
    test_page.enter_content_post(new_post_create[2])
    time.sleep(2)
    test_page.click_save_post_button()
    test_text = test_page.check_title_after_create()
    assert  test_text == new_post_create[0]

def test_load_contact_us_form(browser, contact_us_header_text):
    test_page = OperationsHelper(browser)
    time.sleep(2)
    test_page.click_link_contact()
    time.sleep(8)
    header = test_page.check_contact_form_load()
    assert header == contact_us_header_text

def test_fill_fields_contact_form(browser, contact_us_data):
    test_page = OperationsHelper(browser)
    test_page.enter_contact_name(contact_us_data[0])
    test_page.enter_contact_email(contact_us_data[1])
    test_page.enter_contact_content(contact_us_data[2])
    print(f"{contact_us_data}")
    time.sleep(2)
    name, email, content = test_page.check_filled_contact_form()
    print(f"{name}, {email}, {content}")
    assert name == contact_us_data[0] and \
            email == contact_us_data[1] and \
            content == contact_us_data[2]

def test_check_alert(browser, alert_text):
    test_page = OperationsHelper(browser)
    test_page.click_contact_us_btn()
    time.sleep(8)
    alert = browser.switch_to.alert
    alert_message = alert.text
    print(alert_message)
    assert alert_message == alert_text

