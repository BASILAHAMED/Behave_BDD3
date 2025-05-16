from behave import given, when, then
from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given('the user is on the OrangeHRM login page')
def step_given_login_page(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.page = LoginPage(context.driver)
    context.page.open_login_page()

@when('the user enters username "{username}" and password "{password}"')
def step_when_enter_credentials(context, username, password):
    context.page.enter_credentials(username, password)
    context.page.click_login()

@then('login should "{result}"')
def step_then_check_result(context, result):
    if result == "success":
        assert context.page.is_dashboard_loaded(), "Expected dashboard after login"
    else:
        assert context.page.is_login_failed(), "Expected login failure message"
