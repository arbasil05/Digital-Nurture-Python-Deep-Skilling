import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@pytest.mark.parametrize('message', ['Hello', 'Selenium Automation', '12345'])
def test_simple_form_submission(driver, base_url, message):
    driver.get(f"{base_url}simple-form-demo")
    wait = WebDriverWait(driver, 10)
    
    msg_input = wait.until(EC.visibility_of_element_located((By.ID, "user-message")))
    msg_input.send_keys(message)
    
    show_btn = driver.find_element(By.ID, "showInput")
    driver.execute_script("arguments[0].click();", show_btn)
    
    display_msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    
    assert display_msg.text == message, f"Expected '{message}', got '{display_msg.text}'"


def test_checkbox_demo(driver, base_url):
    driver.get(f"{base_url}checkbox-demo")
    wait = WebDriverWait(driver, 10)
    
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]")))
    
    assert not checkbox.is_selected(), "Checkbox should NOT be selected initially"
    
    driver.execute_script("arguments[0].click();", checkbox)
    assert checkbox.is_selected(), "Checkbox should be selected after click"
    
    driver.execute_script("arguments[0].click();", checkbox)
    assert not checkbox.is_selected(), "Checkbox should be deselected after second click"


def test_dropdown_selection(driver, base_url):
    driver.get(f"{base_url}select-dropdown-demo")
    wait = WebDriverWait(driver, 10)
    
    dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "select-demo")))
    dropdown = Select(dropdown_element)
    
    dropdown.select_by_visible_text("Wednesday")
    
    assert dropdown.first_selected_option.text == "Wednesday", "Selected option text should be 'Wednesday'"
