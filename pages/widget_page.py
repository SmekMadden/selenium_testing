import random
import time

from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from locators.widget_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    loc = AccordianPageLocators()

    accordian_valid_data = {
        1: {'title': 'What is Lorem Ipsum?',
            'content_len': 574},
        2: {'title': 'Where does it come from?',
            'content_len': 763},
        3: {'title': 'Why do we use it?',
            'content_len': 613}
    }

    def get_accordian_data(self, num):

        accordian = {
            1: {
                'title': self.loc.FIRST_SECTION,
                'content': self.loc.FIRST_SECTION_CONTENT},
            2: {
                'title': self.loc.SECOND_SECTION,
                'content': self.loc.SECOND_SECTION_CONTENT},
            3: {
                'title': self.loc.THIRD_SECTION,
                'content': self.loc.THIRD_SECTION_CONTENT}
        }

        title = self.element_is_visible(accordian[num]['title'])

        try:
            self.element_is_visible(accordian[num]['content'])
        except TimeoutException:
            title.click()

        content = self.element_is_visible(accordian[num]['content']
                                          )
        return title.text, content.text

    def assert_actual_data_with_valid_data(self, title, content, acc_num):
        assert title == self.accordian_valid_data[acc_num]['title'], \
            'Wrong title'
        assert len(content) == self.accordian_valid_data[acc_num]['content_len'], \
            'Wrong content'


class AutocompletePage(BasePage):
    loc = AutoCompletePageLocators
    colors = ['Green', 'Black', 'White', 'Red', 'Blue']

    def fill_input_multi(self):
        input_multi = self.element_is_visible(self.loc.MULTI_FIELD)
        for i in range(random.randrange(len(self.colors))):
            random_color = random.choice(self.colors)
            input_multi.send_keys(random_color[0:2])
            input_multi.send_keys(Keys.ENTER)

    def fill_input_single(self):
        input_multi = self.element_is_visible(self.loc.SINGLE_FIELD)
        random_color = random.choice(self.colors)
        input_multi.send_keys(random_color)
        input_multi.send_keys(Keys.ENTER)
