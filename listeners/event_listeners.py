from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class MyEventListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        pass
