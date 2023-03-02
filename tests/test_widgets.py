import random

from pages.widget_page import AccordianPage, AutocompletePage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            page = AccordianPage(driver, 'https://demoqa.com./accordian')
            page.open()

            for accordian_number in [1, 2, 3]:
                title, content = page.get_accordian_data(accordian_number)
                page.assert_actual_data_with_valid_data(title, content, accordian_number)

    class TestAutoCompletePage:
        def test_autocomplete(self, driver):
            page = AutocompletePage(driver, 'https://demoqa.com./auto-complete')
            page.open()
            page.fill_input_multi()
            page.fill_input_single()
