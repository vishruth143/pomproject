from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class GeneraiLib:
    # Scroll web page up by pressing Ctrl+Home
    @staticmethod
    def scroll_up(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.HOME).key_up(Keys.HOME).key_up(Keys.CONTROL).perform()

    # Scroll web page down by pressing Ctrl+End
    @staticmethod
    def scroll_up(driver: WebDriver):
        ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.END).key_up(Keys.END).key_up(Keys.CONTROL).perform()

    # Scroll for web element to view
    @staticmethod
    def scroll_into_view(driver: WebDriver, element: WebElement):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    # Move to web element
    @staticmethod
    def move_to_element(driver: WebDriver, element: WebElement):
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
