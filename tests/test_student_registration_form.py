import time

import pages.student_registration_page
from pages.student_registration_page import RegistrationForm


class TestRegistrationForm:
    def test_form(self, driver):
        page = RegistrationForm(driver, 'https://demoqa.com./automation-practice-form')
        page.open()
        page.fill_form_fields()
