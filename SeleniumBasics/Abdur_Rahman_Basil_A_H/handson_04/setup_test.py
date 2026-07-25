"""
STEP 24: SELENIUM ARCHITECTURE COMPONENTS
1. WebDriver: The core API that acts as a middleman. It accepts commands from this Python script and sends them directly to the browser's native driver to execute actions.
2. Selenium Grid: A server network that allows you to run your tests on multiple machines and multiple browsers simultaneously (parallel execution).
3. Selenium IDE: A browser extension used for "record and playback" testing. Generates basic code, mostly for beginners.
"""


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()

options.add_argument('--headless')

print("Starting the firefox browser")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install(),options=options))

# STEP 26: ADDING IMPLICIT WAIT
# Same concept as before: this waits globally up to 10 seconds.
# BAD PRACTICE REMINDER: Implicit waits apply to *every* element. If an element is missing, 
# it wastes 10 seconds searching. Explicit waits (waiting on specific conditions) are better.
driver.implicitly_wait(10)

try:
    print("Navigating to LambdaTest Playground...")
    driver.get("https://www.lambdatest.com/selenium-playground/")
    
    print(f"Success! The page title is: {driver.title}")

finally:

    print("Closing Firefox...")
    driver.quit()
