import random
import time
# from selenium.webdriver.support.ui import WebDriverWait as Wait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
import requests
from selenium.webdriver import ActionChains
from generator.generator import generated_person, GeneratePerson
from pages.base_page import BasePage
from locators.element_page_locators import *


# TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
# WebTablesLocators, TestButtonPageLocators

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


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()
    button_name = {'Yes': locators.YES,
                   'Impressive': locators.IMPRESSIVE,
                   'No': locators.NO}

    def click_radio_button(self, locator=None):
        self.element_is_present(locator).click()
        # time.sleep(3)

    def get_button_name(self, locator):
        return self.element_is_visible(locator).text

    def get_button_name_from_success_message(self):
        return self.element_is_present(self.locators.SUCCESS_TEXT).text

    def validate_button(self, locator):
        self.click_radio_button(locator)
        name = self.get_button_name(locator)
        assert name == self.get_button_name_from_success_message(), \
            'Clicked button and result do not match'


class WebTables(BasePage):
    locators = WebTablesLocators

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.last_registered_person = []
        self.persons_table = []

    def open_registration_form(self):
        self.element_is_present(self.locators.ADD_BUTTON).click()

    def fill_registration_form(self):
        person = GeneratePerson('ru_RU').result

        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(person['firstname'])
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(person['lastname'])
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person['age'])
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person['email'])
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(person['salary'])
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(person['department'])
        self.element_is_visible(self.locators.SUBMIT_BTN).click()
        for item in ('firstname', 'lastname', 'age', 'email', 'salary', 'department'):
            self.last_registered_person.append(str(person[item]))

        return self.last_registered_person

    def get_persons_from_table(self):
        people_list = self.elements_are_present(self.locators.ALL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        self.persons_table = data

    def check_registered_person_in_table(self):
        print(f'\n {self.last_registered_person}\n{self.persons_table}')
        assert self.last_registered_person in self.persons_table, \
            'Registered person is not in table'

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(key_word)

    def search_registered_person(self):
        # Search by random person attribute
        attribute = random.randrange(len(self.last_registered_person))
        self.search_some_person(self.last_registered_person[attribute])

    def get_person_data(self):
        del_btn = self.element_is_present(self.locators.DELETE_BUTTON)
        return del_btn.find_element(*self.locators.ROW_PARENT).text.splitlines()

    @staticmethod
    def verify_that_data_matches(data1, data2):
        assert data1 == data2, \
            'Data does not match with registered person'


class ButtonsPage(BasePage):
    loc = TestButtonPageLocators

    def click_double_click_button(self):
        btn = self.element_is_present(self.loc.DOUBLE_CLICK)
        self.action_double_click(btn)

    def click_right_click_button(self):
        btn = self.element_is_visible(self.loc.RIGHT_CLICK)
        self.action_right_click(btn)

    def click_click_me_button(self):
        self.element_is_visible(self.loc.CLICK_ME).click()

    def double_click_message_is_presented(self):
        return self.element_is_present(self.loc.DOUBLE_CLK_MESSAGE)

    def right_click_message_is_presented(self):
        return self.element_is_present(self.loc.RIGHT_CLK_MESSAGE)

    def click_me_message_is_presented(self):
        return self.element_is_present(self.loc.CLICK_ME_MESSAGE)


class LinksPage(BasePage):
    loc = LinkPageLocators()

    def check_link_that_open_new_tab(self, locator, status_code):
        link = self.element_is_visible(locator)
        href_url = link.get_attribute('href')
        self.assert_status_code(href_url, status_code)
        link.click()
        self.switch_to_the_new_tab()
        assert href_url == self.driver.current_url, 'href link and opened page link are not equal'
        self.driver.close()
        self.switch_to_the_first_tab()

    def check_home_link(self):
        self.check_link_that_open_new_tab(self.loc.SIMPLE_LINK, 200)

    def check_dynamic_link(self):
        self.check_link_that_open_new_tab(self.loc.DYNAMIC_LINK, 200)

    def check_an_api_call_link(self, locator, status_code):
        link = self.element_is_visible(locator)
        href_url = link.get_attribute('href')
        self.assert_status_code(href_url, status_code)

    def check_created_link(self):
        self.check_an_api_call_link(self.loc.CREATED, 201)

    def check_no_content_link(self):
        self.check_an_api_call_link(self.loc.NO_CONTENT, 204)

    def check_moved_link(self):
        self.check_an_api_call_link(self.loc.MOVED, 301)

    def check_bad_request_link(self):
        self.check_an_api_call_link(self.loc.BAD_REQUEST, 400)

    def check_unauthorized_link(self):
        self.check_an_api_call_link(self.loc.UNAUTHORIZED, 401)

    def check_forbidden_link(self):
        self.check_an_api_call_link(self.loc.FORBIDDEN, 403)

    def check_not_found_link(self):
        self.check_an_api_call_link(self.loc.NOT_FOUND, 404)
