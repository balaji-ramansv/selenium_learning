from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_element(self, locator_type, locator_string):
        time.sleep(1)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator_type, locator_string)))
            return element
        except NoSuchElementException as e:
            print(f"Element with type {locator_type} and string {locator_string} was not found. {e}")
    
    def enter_text(self, locator_type, locator_string, text):
        self.get_element(locator_type, locator_string).send_keys(text)
    
    def click(self, locator_type, locator_string):
        self.get_element(locator_type, locator_string).click()
    
    def select_checkbox(self, locator_type, locator_string):
        self.click(locator_type, locator_string)
    
    def select_radio(self, locator_type, locator_string):
        self.click(locator_type, locator_string)
    
    def submit(self, locator_type, locator_string):
        self.get_element(locator_type, locator_string).submit()
    
    def get_page_title(self):
        return self.driver.title
    
    def select_an_option_from_dropdown(self, locator_type, locator_string, option):
        dropdown_element = self.get_element(locator_type, locator_string)
        select = Select(dropdown_element)
        select.select_by_value(option)

class TheGoldBugsPage(BasePage):
    pass
