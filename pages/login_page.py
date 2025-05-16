from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.web_locators import LoginLocators

class LoginPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_login_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_credentials(self, username, password):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.username)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(LoginLocators.password)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(LoginLocators.login_button)).click()

    def is_dashboard_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(LoginLocators.dashboard))
            return True
        except TimeoutException:
            return False

    def is_login_failed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(LoginLocators.error_message))
            return True
        except TimeoutException:
            return False
