import random

from pages.widget_page import AccordianPage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            page = AccordianPage(driver, 'https://demoqa.com./accordian')
            page.open()

            title, content = page.get_accordian_data(1)
            page.assert_actual_data_with_valid_data(title, content, 1)

            title, content = page.get_accordian_data(2)
            page.assert_actual_data_with_valid_data(title, content, 2)

            title, content = page.get_accordian_data(3)
            page.assert_actual_data_with_valid_data(title, content, 3)
