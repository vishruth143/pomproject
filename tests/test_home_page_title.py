from pages.login_page import LoginPage
from lib.commonfunctions import CommonFunctions
import settings as s
from utilities.custom_logger import Logger
from utilities.loaders import load_xlsx


class TestHomePageTitle(Logger):

    def test_login_page_title(self, driver_setup, tests_setup):
        log = self.get_logger()
        self.data = tests_setup
        test_data = [x for x in self.data['test_home_page_title'] if x['Run?'] == 'Y']

        for i in range(len(test_data)):

            self.driver = driver_setup

            # Libraries needed
            commonfunctions = CommonFunctions(self.driver, test_data, i)

            # Pages needed
            loginpage = LoginPage(self.driver)

            log.info("Launching application url.")
            self.driver.get(s.qa_baseurl)
            log.info("Launching of application url successful.")

            actual_title = self.driver.title
            expected_title = 'Your store. Login'

            if actual_title == expected_title:
                log.info("'Home Page Title' test passed.")
                assert True
            else:
                log.info("'Home Page Title' failed.")
                assert False
