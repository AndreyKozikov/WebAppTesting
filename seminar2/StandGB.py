import yaml
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

class StandGB:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = config['url']

    def find_element(self, locator, time=20):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                     message=f'Element {locator} not found')
        except TimeoutException:
            return None

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def get_web_page(self):
        return self.driver.get(self.base_url)