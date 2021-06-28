from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@given("Open Amazon T&C 508008 page")
def amazon_page (context):
    context.original_window = context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original window")
def store_window(context):
    context.original_window = context.driver.current_window_handle


@when("Click on Amazon Privacy Notice link")
def click_link(context):
 context.driver.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()


@when("Switch to the newly opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window= context.driver.window_handle[1]
    context.driver.switch_to.window(new_window)


@then("Verify Amazon Privacy Notice Page is opened")
def privacy_page(context):
    assert "https://www.amazon.com/gp/help/customer/"in context.driver_url, f"url ttps://www.amazon.com/gp/help/customer/ not in {context.driver}"



@when("User can close new window")
def close_window(context):

    context.driver.close()

@when("switch back to original")
def switch_to_original_window(context):
   original_window= context.driver.window_handle[1]
   context.driver.switch_to_original_window(original_window)

