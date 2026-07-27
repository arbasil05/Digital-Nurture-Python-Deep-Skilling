from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage

class CheckboxPage(BasePage):
    CHECKBOX_TEMPLATE = (By.XPATH, "(//input[@type='checkbox'])[{}]")

    def get_checkbox_locator(self, index):
        return (self.CHECKBOX_TEMPLATE[0], self.CHECKBOX_TEMPLATE[1].format(index))

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def check_option(self, index):
        locator = self.get_checkbox_locator(index)
        checkbox = self.wait_for_clickable(locator)
        if not checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def uncheck_option(self, index):
        locator = self.get_checkbox_locator(index)
        checkbox = self.wait_for_clickable(locator)
        if checkbox.is_selected():
            self.driver.execute_script("arguments[0].click();", checkbox)

    def is_option_checked(self, index):
        locator = self.get_checkbox_locator(index)
        checkbox = self.wait_for_clickable(locator)
        return checkbox.is_selected()
