from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

print("Starting Firefox")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.implicitly_wait(10)

try:
    current_size = driver.get_window_size()
    print(f"Original Window Size : {current_size}")

    driver.set_window_size(1280,800)

    print("Navigating to Playground...")
    driver.get("https://www.lambdatest.com/selenium-playground/")

    print("Clicking 'Simple Form Demo' link...")
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    print("Checking if the URL is correct...")
    assert "simple-form-demo" in driver.current_url


    print("Going back to the previous page...")
    driver.back()

    print("Opening a new tab for Google...")
    driver.execute_script('window.open("https://www.google.com");')


    tabs = driver.window_handles 
    
    print("Switching focus to the new Google tab...")
    driver.switch_to.window(tabs[1])
    
    print(f"We are now on: {driver.title}")

    print("Switching back to the original Playground tab...")
    driver.switch_to.window(tabs[0])

    print("Taking a screenshot...")
    driver.save_screenshot('playground_screenshot.png')
    print("Screenshot saved as 'playground_screenshot.png'!")
finally:
    print("Test complete. Closing Firefox...")
    driver.quit()
