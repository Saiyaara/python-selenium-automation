from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver



@given('Open Amazon product B07F2N8KWH page')
def open_amazon_product_page(context):
 product_id = context.driver.get('https://www.amazon.com/dp/B07F2N8KWH?th=1')

@then('verify user can click through colors')
def verify_user_click_color(context):
 expected_colors = ['Black', 'Blue', 'Gray', 'Grey Pineapple', 'Grey Plaid', 'Khaki', 'Khaki Anchor', 'Khaki Plaid', 'Navy' 'Navy Anchor', 'Navy Plaid', 'Olive', 'Olive Plaid', 'Silver', 'Stone', 'Washed Red','Washed Red Lobster']
 color_webelements = context.driver.find_elements(By.CSS_SELECTOR,"#variation_color_name li")

 for i in range(len(color_webelements)):
  color_webelements[i].click()
  actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text

 assert actual_text == expected_colors, f'Error, color is {actual_text}, but expected {expected_colors[i]}'
