from generators.generator import GenerateFile
from pages.elements_page import *


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


class TestButtons:
    def test_buttons_click(self, driver):
        page = ButtonsPage(driver, 'https://demoqa.com./buttons')
        page.open()
        # separately to better localize
        page.click_double_click_button()
        print(page.double_click_message_is_presented().text)
        page.click_right_click_button()
        print(page.right_click_message_is_presented().text)
        page.click_click_me_button()
        print(page.click_me_message_is_presented().text)


class TestLinks:

    def test_check_link(self, driver):
        page = LinksPage(driver, 'https://demoqa.com./links')
        page.open()
        page.check_home_link()
        page.check_dynamic_link()

    def test_broken_links(self, driver):
        page = LinksPage(driver, 'https://demoqa.com./links')
        page.open()
        page.check_created_link()
        page.check_no_content_link()
        page.check_moved_link()
        page.check_bad_request_link()
        page.check_unauthorized_link()
        page.check_forbidden_link()
        page.check_not_found_link()


class TestUploadAndDownload:
    def test_upload_file(self, driver):
        page = UploadAndDownloadPage(driver, 'https://demoqa.com./upload-download')
        page.open()
        file = GenerateFile()
        try:
            file.create_file()
            page.upload_file(file.file_path)
            page.assert_result_filename_equal_filename(file.file_name)
        finally:
            file.delete_file()

    def test_download_file(self, driver):
        page = UploadAndDownloadPage(driver, 'https://demoqa.com./upload-download')
        page.open()
        file_path = page.download_file()
        assert os.path.exists(file_path), 'File is not downloaded'
        os.remove(file_path)
