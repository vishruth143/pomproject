import random
from faker import Faker
from datetime import datetime
from pages.login_page import LoginPage
import settings as s


class CommonFunctions:

    @staticmethod
    def fake_name():
        return Faker().name()

    @staticmethod
    def fake_first_name():
        return Faker().first_name()

    @staticmethod
    def fake_last_name():
        return Faker().last_name()

    @staticmethod
    def fake_ssn():
        return Faker().ssn().replace('-', '')

    @staticmethod
    def fake_phonenumber():
        return str(random.randint(2220000000, 2229999999))

    @staticmethod
    def get_date():
        return datetime.today().strftime('%m-%d-%Y')

    def __init__(self, driver, test_data, i):
        self.driver = driver
        self.test_data = test_data
        self.i = i

        # Pages needed
        self.loginpage = LoginPage(self.driver)

    def login(self):
        if s.REGION == 'QA':
            self.loginpage.type_email_txt(self.test_data[self.i]['Email'])
            self.loginpage.type_password_txt(s.qa_password)
            self.loginpage.click_login_btn()
