import time

from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.element_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('sfsdfg')
        self.element_is_visible(self.locators.EMAIL).send_keys('sdgsdg@sfaf.com')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('sdgsga')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('sdgasg')
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        time.sleep(5)
