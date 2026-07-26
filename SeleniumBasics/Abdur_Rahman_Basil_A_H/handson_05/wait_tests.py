import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

print("Starting Firefox...")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

try:
    driver.maximize_window()

    print("Navigating to Bootstrap Alert Demo...")
    driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
    
    wait = WebDriverWait(driver, 10)
    
    normal_success_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Normal Success Message')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", normal_success_btn)
    normal_success_btn.click()

    alert_box = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success-manual"))
    )
    
    print(f"Alert Text Found: '{alert_box.text.strip()}'")
    assert "success" in alert_box.text.lower()
    print("Step 36 & 38 Complete: Explicit waits verified successfully!")

    print("\n--- Step 37: Running Timing Benchmark ---")
    
    driver.refresh()
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    start_sleep = time.time()
    
    btn_sleep = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Normal Success Message')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_sleep)
    btn_sleep.click()
    
    time.sleep(3)
    
    alert_sleep = driver.find_element(By.CSS_SELECTOR, ".alert-success-manual")
    _ = alert_sleep.text
    
    elapsed_sleep = time.time() - start_sleep
    print(f" -> time.sleep(3) approach took: {elapsed_sleep:.4f} seconds")

    driver.refresh()
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
    start_explicit = time.time()
    
    btn_explicit = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Normal Success Message')]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_explicit)
    btn_explicit.click()
    
    alert_explicit = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success-manual"))
    )
    _ = alert_explicit.text
    
    elapsed_explicit = time.time() - start_explicit
    print(f" -> Explicit Wait approach took: {elapsed_explicit:.4f} seconds")

    print(f" -> Result: Explicit wait was {elapsed_sleep - elapsed_explicit:.4f} seconds faster!")

    print("\n--- Step 39: Running Fluent Wait ---")
    driver.get("https://www.lambdatest.com/selenium-playground/dynamic-data-loading-demo")

    fluent_wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5,
        ignored_exceptions=[NoSuchElementException, ElementNotVisibleException]
    )

    get_user_btn = fluent_wait.until(
        EC.element_to_be_clickable((By.ID, "save"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", get_user_btn)
    get_user_btn.click()

    user_container = fluent_wait.until(
        EC.visibility_of_element_located((By.ID, "loading"))
    )
    print(f" -> Dynamically loaded content found: {user_container.text.strip()}")
    print("Step 39 Complete: Fluent Wait polling verified!")

finally:
    print("\nClosing Firefox...")
    driver.quit()