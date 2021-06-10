from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Return web element
    def return_web_element(self, locator_type, locator, howtowait, wait_time=60):
        if howtowait == "visibility_of_element_located":
            return WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located((locator_type, locator)))
        if howtowait == "element_to_be_clickable":
            return WebDriverWait(self.driver, wait_time).until(ec.element_to_be_clickable((locator_type, locator)))
        if howtowait == "presence_of_element_located":
            return WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located((locator_type, locator)))

    # Return web elements
    def return_web_elements(self, locator_type, locator):
        return self.driver.find_elements(locator_type, locator)

    # Click on web element
    def click(self, element):
        element.click()

    # Select the dropdown by visible text
    def select(self, element, value):
        Select(element).select_by_visible_text(value)

    # Get the text of the web element
    def get_text(self, element):
        return element.text

    # Type into the text box
    def type(self, element, value):
        element.clear()
        element.send_keys(value)

    # Web element is enabled
    def enabled(self, element):
        return element.is_enabled()

    # Web element is displayed
    def displayed(self,locator_type, locator, howtowait, wait_time=60):
        if howtowait == "visibility_of_element_located":
            return WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located((locator_type, locator))).is_displayed()
        if howtowait == "element_to_be_clickable":
            return WebDriverWait(self.driver, wait_time).until(ec.element_to_be_clickable((locator_type, locator))).is_displayed()

    # Web element exists?
    def exists(self, locator_type, locator):
        if locator_type == By.XPATH:
            try:
                self.driver.find_element_by_xpath(locator)
            except NoSuchElementException:
                return False
            return True
        elif locator_type == By.CSS_SELECTOR:
            try:
                self.driver.find_element_by_css_selector(locator)
            except NoSuchElementException:
                return False
            return True
