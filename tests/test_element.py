import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTables


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


class TestRadioButton:
    def test_radio_button(self, driver):
        page = RadioButtonPage(driver, 'https://demoqa.com./radio-button')
        page.open()
        page.validate_button(page.button_name['Yes'])
        page.validate_button(page.button_name['Impressive'])
        page.validate_button(page.button_name['No'])  # bug!


class TestWebTables:
    def test_web_table_add_person(self, driver):
        page = WebTables(driver, 'https://demoqa.com./webtables')
        page.open()
        page.open_registration_form()
        page.fill_registration_form()
        page.get_persons_from_table()
        page.check_registered_person_in_table()

    def test_web_table_search_person(self, driver):
        page = WebTables(driver, 'https://demoqa.com./webtables')
        page.open()
        page.open_registration_form()
        reg_person_data = page.fill_registration_form()
        page.search_registered_person()
        person_data = page.get_person_data()
        page.verify_that_data_matches(reg_person_data, person_data)
