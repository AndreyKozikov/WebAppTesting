import yaml
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

with open("config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

@pytest.mark.usefixtures("setup_class")
class StandGB:
    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(config['wait_time'])

    def find_element(self, locator, time=20):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                     message=f'Element {locator} not found')
        except TimeoutException:
            return None

    def wait_element_stay_invisible(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def get_element_property(self, locator, prop):
        element = self.find_element(locator)
        return element.value_of_css_property(prop)

    def get_element_value(self, locator):
        element = self.find_element(locator)
        return element.get_attribute('value')

    def get_web_page(self, url):
        return self.driver.get(url)