from Utilities import Locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from Utilities.customLogger import GetLogger
import time
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.__logger = GetLogger.get_Logger(file=".//Logs/test_login.log")


    def SignIn(self, username, password, keep_sign_in = False):
        account_ele = self.driver.find_element_by_xpath(
            Locators.MainPage_Locators["account_and_list_xpath"])
        ActionChains(self.driver).move_to_element(account_ele)
        signin_status = self.driver.find_element_by_xpath(
            Locators.MainPage_Locators["sign_in_xpath"])
        if not signin_status:
            self.driver.save_screenshot(".//Screenshots/sign_in_button_not_found.png")
            self.__logger.warn("Sign in button not found. The user might have already signed in")
        account_ele.click()
        time.sleep(5)
        self.__logger.info("Enter Email and click on continue")
        email_ele = self.driver.find_element_by_name(Locators.LoginPage_Locators["email_name"])
        email_ele.click()
        time.sleep(5)
        email_ele.clear()
        email_ele.send_keys(username)
        time.sleep(3)
        self.driver.save_screenshot(".//Screenshots/entered_username.png")
        self.driver.find_element_by_id(Locators.LoginPage_Locators['continue_id']).click()
        time.sleep(3)
        '''alert_ele = self.driver.find_element_by_class_name(Locators.LoginPage_Locators['alert_class_name'])
        if "We cannot find an account with that email" in alert_ele.text:
            raise Exception("Wrong email address entered")'''
        self.__logger.info("Continuing to enter Password")
        password_ele = self.driver.find_element_by_name(Locators.LoginPage_Locators['password_name'])
        password_ele.click()
        password_ele.clear()
        password_ele.send_keys(password)
        time.sleep(3)
        self.driver.save_screenshot(".//Screenshots/entered_password.png")
        if keep_sign_in:
            self.driver.find_element_by_name(Locators.LoginPage_Locators['keep_sign_in_name']).click()
            self.__logger.info("Keep me Signed In checked!")
            self.driver.save_screenshot("//Screenshots/keep_sign_in_true.png")
        self.__logger.info("Clicking on Sign-in")
        status = self.driver.find_element_by_id(Locators.LoginPage_Locators['sign_in_button_id']).submit()
        '''alert_ele = self.driver.find_element_by_class_name(Locators.LoginPage_Locators['alert_class_name'])
        if "Your password is incorrect" in alert_ele.text:
            raise Exception("Password entered is incorrect!!")'''
        if not status:
            self.driver.save_screenshot(".//Screenshots/Login_failed.png")
            self.__logger.error("Login failed!")
            s = False
        self.__logger.info("Login Successful")
        self.driver.save_screenshot(".//Screenshots/Login_successful.png")
        s = True
        return s

    def maximize_minimise(self, action="Maximize"):
        if action == "Maximize":
            self.driver.maximize_window()
            time.sleep(3)
            self.__logger.info("Successfully maximized window")
        else:
            self.driver.minimize_window()
            time.sleep(3)
            self.__logger.info("Successfully minimized window")










