import time
import requests
from StandGB import StandGB
from selenium.webdriver.common.by import By
import yaml
import logging


class SearchLocators:
    ids = dict()
    with open("locators.yaml", "r") as f:
        locators = yaml.safe_load(f)
    if locators["XPATH"]:
        for locator in locators["XPATH"].keys():
            ids[locator] = (By.XPATH, locators["XPATH"][locator])
    if locators["CSS"]:
        for locator in locators["CSS"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["CSS"][locator])


class OperationsHelper(StandGB):
    def check_success_login(self):
        return self.find_element(SearchLocators.ids["LOCATOR_SUCCESS_LOGIN"]).text

    def enter_login(self, login):
        logging.info(f"Send '{login}' to element {SearchLocators.ids['LOCATOR_LOGIN_FIELD']}")
        login_field = self.find_element(SearchLocators.ids["LOCATOR_LOGIN_FIELD"])
        if not login_field:
            logging.error("Login field not found")
            return False
        try:
            login_field.clear()
            login_field.send_keys(login)
        except:
            logging.exception("Exception while operation with login field")


    def enter_password(self, password):
        password_field = self.find_element(SearchLocators.ids["LOCATOR_PASSWORD_FIELD"])
        if not password_field:
            logging.error("Password field not found")
            return False
        try:
            password_field.clear()
            password_field.send_keys(password)
        except:
            logging.exception("Exception while operation with password field")

    def click_login_button(self, wait=False):
        try:
            self.find_element(SearchLocators.ids["LOCATOR_LOGIN_BUTTON"]).click()
            if wait:
                self.wait_element_stay_invisible(SearchLocators.ids["LOCATOR_LOGIN_BUTTON"])
        except:
            logging.exception("Exception while click login button")

    def get_error_message(self):
        try:
            error_text = self.find_element(SearchLocators.ids["LOCATOR_ERROR_FIELD"]).text
            return error_text
        except:
            return None

    def click_create_post_button(self):
        try:
            self.find_element(SearchLocators.ids["LOCATOR_CREATE_POST_BTN"]).click()
            self.wait_element_stay_invisible(SearchLocators.ids["LOCATOR_CREATE_POST_BTN"])
        except:
            logging.exception("Exception while click create post button")

    def enter_title_post(self, title):
        title_field = self.find_element(SearchLocators.ids["LOCATOR_TITLE_POST_FIELD"])
        if not title_field:
            logging.error("Title field in post creation form not found")
            return False
        try:
            title_field.clear()
            title_field.send_keys(title)
        except:
            logging.exception("Exception while operation with title field in post creation form")

    def enter_content_post(self, content):
        content_field = self.find_element(SearchLocators.ids["LOCATOR_CONTENT_POST_FIELD"])
        content_field.clear()
        content_field.send_keys(content)

    def enter_desc_post(self, desc):
        desc_field = self.find_element(SearchLocators.ids["LOCATOR_DESC_POST_FIELD"])
        desc_field.clear()
        desc_field.send_keys(desc)

    def click_save_post_button(self):
        self.find_element(SearchLocators.ids["LOCATOR_SAVE_POST_BTN"]).click()
        self.wait_element_stay_invisible(SearchLocators.ids["LOCATOR_SAVE_POST_BTN"])

    def check_title_after_create(self):
        self.wait_element_stay_invisible(SearchLocators.ids["LOCATOR_SAVE_POST_BTN"])
        title = self.find_element(SearchLocators.ids["LOCATOR_TITLE_AFTER_CREATE"]).text
        return  title

    def click_link_contact(self):
        self.find_element(SearchLocators.ids["LOCATOR_HREF_CONTACT_US"]).click()

    def check_contact_form_load(self):
        return self.find_element(SearchLocators.ids["LOCATOR_H1_CONTACT_US"]).text

    def enter_contact_name(self, name):
        name_field = self.find_element(SearchLocators.ids["LOCATOR_CONTACT_YOU_NAME_FIELD"])
        name_field.clear()
        name_field.send_keys(name)

    def enter_contact_email(self, email):
        email_field = self.find_element(SearchLocators.ids["LOCATOR_CONTACT_YOU_EMAIL_FIELD"])
        email_field.clear()
        email_field.send_keys(email)

    def enter_contact_content(self, contact):
        content_filed = self.find_element(SearchLocators.ids["LOCATOR_CONTACT_CONTENT_FIELD"])
        content_filed.clear()
        content_filed.send_keys(contact)

    def click_contact_us_btn(self):
        self.find_element(SearchLocators.ids["LOCATOR_CONTACT_US_BTN"]).click()

    def check_filled_contact_form(self):
        name = self.get_element_value(SearchLocators.ids["LOCATOR_CONTACT_YOU_NAME_FIELD"])
        email = self.get_element_value(SearchLocators.ids["LOCATOR_CONTACT_YOU_EMAIL_FIELD"])
        content = self.get_element_value(SearchLocators.ids["LOCATOR_CONTACT_CONTENT_FIELD"])
        return name, email, content


class OperationsHelperApi:
    # Создание нового поста
    def create_post_api(api_session, url, data):
        response = api_session.post(url + "api/posts", data=data)
        if response.status_code < 200 or response.status_code > 299:
            logging.error(f"Failed to create post: {response.status_code} - {response.text}")
        return data["description"]
