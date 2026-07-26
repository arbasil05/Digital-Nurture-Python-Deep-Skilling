import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"

@pytest.fixture(scope="function")
def driver(request):
    print("\n[SETUP] Starting Firefox for test...")
    driver_instance = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver_instance.maximize_window()
    
    # Attach driver to request.node so we can access it in the makereport hook
    request.node.driver = driver_instance
    
    yield driver_instance 
    
    print("\n[TEARDOWN] Closing Firefox after test...")
    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            screenshot_path = f"{item.name}_failure.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n[FAILURE] Screenshot saved to {screenshot_path}")
