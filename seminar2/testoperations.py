from StandGB import StandGB
from selenium.webdriver.common.by import By

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASSWORD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/div[3]/button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, '#create-btn')
    LOCATOR_TITLE_POST_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_DESC_POST_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT_POST_FIELD = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_SAVE_POST_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button')
    LOCATOR_TITLE_AFTER_CREATE = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_SUCCESS_LOGIN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')

class TestOperations(StandGB):
    def check_success_login(self):
        return self.find_element(TestSearchLocators.LOCATOR_SUCCESS_LOGIN).text

    def enter_login(self, login):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login)

    def enter_password(self, password):
        password_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BUTTON).click()

    def get_error_message(self):
        try:
            error_text = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD).text
            return error_text
        except:
            return None

    def click_create_post_button(self):
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_title_post(self, title):
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST_FIELD)
        title_field.clear()
        title_field.send_keys(title)

    def enter_content_post(self, content):
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_POST_FIELD)
        content_field.clear()
        content_field.send_keys(content)

    def enter_desc_post(self, desc):
        desc_field = self.find_element(TestSearchLocators.LOCATOR_DESC_POST_FIELD)
        desc_field.clear()
        desc_field.send_keys(desc)

    def click_save_post_button(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def check_title_after_create(self):
        title = self.find_element(TestSearchLocators.LOCATOR_TITLE_AFTER_CREATE).text
        return  title

