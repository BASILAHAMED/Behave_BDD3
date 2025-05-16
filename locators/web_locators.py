from selenium.webdriver.common.by import By

class LoginLocators:
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    dashboard = (By.XPATH, "//h6[text()='Dashboard']")
    error_message = (By.XPATH, "//p[text()='Invalid credentials']")
