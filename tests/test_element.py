import time

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestTextBox:

    def test_text_box(self, driver):
        page = TextBoxPage(driver, 'https://demoqa.com./text-box')
        page.open()
        inp_name, inp_email, inp_cur_address, inp_perm_address = page.fill_all_fields()
        out_name, out_email, out_cur_address, out_perm_address = page.check_fields()
        assert inp_name == out_name, 'names are not match'
        assert inp_email == out_email, 'emails are not match'
        assert inp_cur_address == out_cur_address, 'current addresses are not match'
        assert inp_perm_address == out_perm_address, 'permanent addresses are not match'


class TestCheckBox:
    def test_check_box(self, driver):
        page = CheckBoxPage(driver, 'https://demoqa.com./checkbox')
        page.open()
        page.open_full_list()
        page.click_random_checkbox()
        page.compare_clicked_checkboxes_with_result_message()
        time.sleep(1)
