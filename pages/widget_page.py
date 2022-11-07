from selenium.common import TimeoutException

from locators.widget_page_locators import AccordianPageLocators
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
