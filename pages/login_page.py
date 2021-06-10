from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # ********************************* Web Elements *********************************
    # --------------------------------- Texts ---------------------------------

    # --------------------------------- Text Boxes ---------------------------------
    @property
    def email_txt(self):
        return self.return_web_element(By.ID, "Email", "visibility_of_element_located")

    @property
    def password_txt(self):
        return self.return_web_element(By.ID, "Password", "visibility_of_element_located")

    # --------------------------------- Links ---------------------------------

    # --------------------------------- Buttons ---------------------------------
    @property
    def login_btn(self):
        return self.return_web_element(By.XPATH, "//button[@type='submit']", "element_to_be_clickable")

    # --------------------------------- Drop Downs ---------------------------------

    # --------------------------------- Images ---------------------------------

    # ********************************* Web Elements Fundtions *********************************
    # --------------------------------- Get Text Functions ---------------------------------

    # --------------------------------- Type Functions ---------------------------------
    def type_email_txt(self, email):
        self.type(self.email_txt, email)

    def type_password_txt(self, password):
        self.type(self.password_txt, password)

    # --------------------------------- Click Functions ---------------------------------
    def click_login_btn(self):
        self.click(self.login_btn)

    # --------------------------------- Displayed Functions ---------------------------------

    # --------------------------------- Exists Functions ---------------------------------
