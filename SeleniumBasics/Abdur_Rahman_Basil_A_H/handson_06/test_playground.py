from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_simple_form_submission(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    wait = WebDriverWait(driver, 10)
    
    msg_input = wait.until(EC.visibility_of_element_located((By.ID, "user-message")))
    msg_input.send_keys("Hello Selenium")
    
    show_btn = driver.find_element(By.ID, "showInput")
    driver.execute_script("arguments[0].click();", show_btn)
    
    display_msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    
    assert display_msg.text == "Hello Selenium", f"Expected 'Hello Selenium', got '{display_msg.text}'"


def test_checkbox_demo(driver):
    driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")
    wait = WebDriverWait(driver, 10)
    
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]")))
    
    assert not checkbox.is_selected(), "Checkbox should NOT be selected initially"
    
    driver.execute_script("arguments[0].click();", checkbox)
    assert checkbox.is_selected(), "Checkbox should be selected after click"
    
    driver.execute_script("arguments[0].click();", checkbox)
    assert not checkbox.is_selected(), "Checkbox should be deselected after second click"