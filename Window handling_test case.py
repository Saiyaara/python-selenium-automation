from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@given("Open Amazon T&C 508088 page")
def amazon_page (context):
    context.original_window = context.driver.current_window_handle

    sleep(1)

@when("Store original windows")
def store_windows(context):
    context.original_window = context.driver.current_window_handle

    sleep(1)


@when("Click on Amazon Privacy Notice link")
def click_link(context):
 context.driver.find_element(By.XPATH,"//a[@href='https://www.amazon.com/privacy']").click()

sleep(1)

@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window= context.driver.window_handle[1]
    context.driver.switch_to.window(new_window)
    sleep(1)

@then("Verify Amazon Privacy Notice Page is opened")
def privacy_page(context):
    assert "https://www.amazon.com/gp/help/customer/"in context.driver_url, f"url ttps://www.amazon.com/gp/help/customer/ not in {context.driver}"

    sleep(1)

@when("User can close new window")
def close_window(context):

    sleep(1)
    context.driver.close()

@when("switch back to original")
def switch_to_original_window(context):
   original_window= context.driver.window_handle[1]
   context.driver.switch_to_original_window(original_window)

sleep(1)
