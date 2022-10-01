import time

from pages.elements_page import TextBoxPage


class TestBox:

    def test_text_box(self, driver):
        page = TextBoxPage(driver, 'https://demoqa.com./text-box')
        page.open()
        inp_name, inp_email, inp_cur_address, inp_perm_address = page.fill_all_fields()
        out_name, out_email, out_cur_address, out_perm_address = page.check_fields()
        # time.sleep(5)
        assert inp_name == out_name, 'names are not match'
        assert inp_email == out_email, 'emails are not match'
        assert inp_cur_address == out_cur_address, 'current addresses are not match'
        assert inp_perm_address == out_perm_address, 'permanent addresses are not match'

        # print(*page.check_fields(), sep='\n')
