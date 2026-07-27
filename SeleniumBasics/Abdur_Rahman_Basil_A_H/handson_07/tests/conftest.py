import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="function")
def driver():
    print("\n[SETUP] Starting Firefox for test...")
    driver_instance = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver_instance.maximize_window()
    
    yield driver_instance 
    
    print("\n[TEARDOWN] Closing Firefox after test...")
    driver_instance.quit()