from behave_webdriver.steps import * # ignore

from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)
    time.sleep(2)

@when('I enter "{text}" in the input field "input"')
def step_enter_text(context, text):
    input_field = context.behave_driver.find_element(By.ID, "letters")
    input_field.clear()
    input_field.send_keys(text)

@when('I enter "{text}" in the input field "shift"')
def step_enter_shift(context, text):
    shift_select = context.behave_driver.find_element(By.ID, "shift-amount")
    shift_select.click()
    option = context.behave_driver.find_element(By.CSS_SELECTOR, f'#shift-amount option[value="{text}"]')
    option.click()

@when('I click the element "{selector}"')
def step_click_element(context, selector):
    if "encode" in selector.lower():
        setting_select = context.behave_driver.find_element(By.ID, "decoder-setting")
        setting_select.click()
        encode_option = context.behave_driver.find_element(By.CSS_SELECTOR, '#decoder-setting option[value="E"]')
        encode_option.click()
    elif "decode" in selector.lower():
        setting_select = context.behave_driver.find_element(By.ID, "decoder-setting")
        setting_select.click()
        decode_option = context.behave_driver.find_element(By.CSS_SELECTOR, '#decoder-setting option[value="D"]')
        decode_option.click()
    
    submit_button = context.behave_driver.find_element(By.ID, "submit")
    submit_button.click()

@when('I wait for "{milliseconds}" ms')
def step_wait_milliseconds(context, milliseconds):
    seconds = float(milliseconds) / 1000
    time.sleep(seconds)

@then('I expect the element "{selector}" to have text "{expected_text}"')
def step_verify_element_text(context, selector, expected_text):
    element = context.behave_driver.find_element(By.ID, "decoded_message")
    actual_text = element.text.strip()
    assert actual_text == expected_text, f"Expected text '{expected_text}' but found '{actual_text}'"