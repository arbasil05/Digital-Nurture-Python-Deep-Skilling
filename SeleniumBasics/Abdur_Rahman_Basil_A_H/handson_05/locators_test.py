"""
STEP 35: RANKING THE 6 LOCATOR STRATEGIES (Best to Worst)

1. By.ID - BEST. IDs are supposed to be 100% unique on a web page. It is the fastest and most reliable way.
2. By.NAME - EXCELLENT. Usually unique (especially in forms) and very reliable.
3. By.CSS_SELECTOR - GREAT. Extremely fast, highly readable, and can easily traverse parent/child relationships. 
4. By.XPATH (Relative) - GOOD. Slower than CSS, but the ONLY locator that can find elements based on inner text.
5. By.CLASS_NAME / By.TAG_NAME - OKAY. Rarely unique. Only use if you intentionally want to grab a list of elements.
6. By.XPATH (Absolute) - TERRIBLE. Never use this. If a developer adds a single new <div>, the entire path breaks.
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

print("Starting Firefox...")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)

try:
    print("Navigating to Simple Form Demo...")
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    element_by_id = driver.find_element(By.ID, "user-message")
    element_by_id.send_keys("Testing ID")
    element_by_id.clear()

    element_by_class = driver.find_element(By.CLASS_NAME, "form-control")

    element_by_tag = driver.find_element(By.TAG_NAME, "input")

    element_by_rel_xpath = driver.find_element(By.XPATH, "//input[@id='user-message']")

    try:
        element_by_abs_xpath = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[2]/div/div/div/div[1]/div[2]/div/div[1]/input")
    except NoSuchElementException:
        print(" -> EXPECTED ERROR: Absolute XPath failed because the page structure changed. Moving on...")

    print("Step 32 Complete: Successfully located elements using basic strategies.")

    css_id = driver.find_element(By.CSS_SELECTOR, "#user-message")

    css_attr = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Please enter your Message']")

    css_parent = driver.find_element(By.CSS_SELECTOR, "div.left-input > input")

    print("Step 33 Complete: CSS Selectors worked.")

    print("Navigating to Checkbox Demo...")
    driver.get("https://www.lambdatest.com/selenium-playground/checkbox-demo")

    exact_text_checkbox = driver.find_element(By.XPATH, "//label[text()='Option 1']")
    print(f" -> Found exact text label: {exact_text_checkbox.text}")

    all_options = driver.find_elements(By.XPATH, "//label[contains(text(), 'Option')]")
    print(f" -> Found {len(all_options)} elements containing the word 'Option'.")

    print("Step 34 Complete: XPath text functions worked.")

finally:
    print("Closing Firefox...")
    driver.quit()