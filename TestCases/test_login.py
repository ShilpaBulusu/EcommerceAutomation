from Page_Objects.LoginPage import LoginPage
import string
import random
from Utilities.readProperties import Config
from Utilities.customLogger import GetLogger
import pytest

@pytest.mark.sanity
class Test_001_Login:

    def test_login(self, setup):
        self.driver, self.logger, self.config = setup
        self.logger.info("*********** test_login ************")
        login_page = LoginPage(self.driver)
        login_page.maximize_minimise()
        if "Online Shopping site" not in self.driver.title:
            raise Exception("Logged in into different site")
        stat = login_page.SignIn(self.config["username"], self.config["password"], self.config["keep_sign_in"])
        if not stat:
            raise Exception("Login failed!!")
        self.logger.info("Login Successful!!!!")

