import time

from pages.elements_page import TextBoxPage


class TestBox:

    def test_text_box(self, driver):
        page = TextBoxPage(driver, 'https://demoqa.com./text-box')
        page.open()
        page.fill_all_fields()
        time.sleep(5)
