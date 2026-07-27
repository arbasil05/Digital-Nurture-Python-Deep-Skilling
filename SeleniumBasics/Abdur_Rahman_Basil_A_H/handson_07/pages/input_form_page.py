from selenium.webdriver.common.by import By
from .base_page import BasePage

class InputFormPage(BasePage):
    NAME_INPUT = (By.ID, 'name')
    EMAIL_INPUT = (By.ID, 'inputEmail4')
    PHONE_INPUT = (By.ID, 'websitename') # Using website field for phone to satisfy the parameter
    ADDRESS_INPUT = (By.ID, 'inputAddress1')
    SUBMIT_BUTTON = (By.XPATH, '//button[text()="Submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.success-msg')

    def fill_form(self, name, email, phone, address):
        self.wait_for_element(self.NAME_INPUT).send_keys(name)
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PHONE_INPUT).send_keys(phone)
        self.wait_for_element(self.ADDRESS_INPUT).send_keys(address)

    def submit_form(self):
        element = self.wait_for_element(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
