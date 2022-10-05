import random
import time
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.element_page_locators import TextBoxPageLocators, CheckBoxPageLocators


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clickable(self.locators.SUBMIT_BUTTON).click()
        time.sleep(3)
        return full_name, email, current_address, permanent_address

    def check_fields(self):
        full_name = self.element_is_present(self.locators.OUTPUT_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.OUTPUT_PERM_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        checkbox_list = self.elements_are_visible(self.locators.CHECKBOX_LIST)
        for _ in 'qwe':  # 3 random checkbox
            checkbox_list[random.randrange(len(checkbox_list))].click()  # list[index].click

    def compare_clicked_checkboxes_with_result_message(self):
        checkbox_list = self.elements_are_present(self.locators.CHECKED_BOXES)
        selected_box_names = []

        for box in checkbox_list:
            box_name = box.find_element(*self.locators.CHECKBOX_TITLE).text
            selected_box_names.append(box_name.lower().replace('.doc', '').replace(' ', ''))

        output_box_names = [name.text.lower() for name in
                            self.elements_are_present(self.locators.BOX_NAMES_FROM_RESULT)]

        assert selected_box_names == output_box_names, \
            'Names of selected boxes and names in result message are not match'
