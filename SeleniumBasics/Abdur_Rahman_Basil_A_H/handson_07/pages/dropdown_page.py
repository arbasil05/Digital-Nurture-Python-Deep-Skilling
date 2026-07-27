from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class DropdownPage(BasePage):
    DAY_DROPDOWN = (By.ID, 'select-demo')
    
    def select_day(self, day_name):
        element = self.wait_for_element(self.DAY_DROPDOWN)
        select = Select(element)
        select.select_by_visible_text(day_name)
