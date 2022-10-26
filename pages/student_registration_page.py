import random

from selenium.webdriver import Keys

from generators.generator import GeneratePerson, GenerateFile
from locators.student_registration_page_locators import RegistrationFormLocators
from pages.base_page import BasePage


class RegistrationForm(BasePage):
    loc = RegistrationFormLocators()

    def fill_form_fields(self):
        # data:
        file = GenerateFile('qwe.png')
        file.create_file()
        person = GeneratePerson('ru_RU').result
        hobbies = (self.loc.SPORT_B, self.loc.READING_B, self.loc.MUSIC_B)

        # form interact:
        self.driver.maximize_window()
        self.element_is_visible(self.loc.FIRSTNAME).send_keys(person['firstname'])
        self.element_is_visible(self.loc.LASTNAME).send_keys(person['lastname'])
        self.element_is_visible(self.loc.EMAIL).send_keys(person['email'])
        self.element_is_visible(
            (self.loc.MALE_RB, self.loc.FEMALE_RB, self.loc.OTHER_RB)[random.randrange(3)]
        ).click()
        self.element_is_visible(self.loc.MOBILE).send_keys(person['mobile'])
        self.element_is_visible(self.loc.SUBJECTS).send_keys('Arts')
        self.element_is_visible(self.loc.SUBJECTS).send_keys(Keys.RETURN)
        [self.element_is_visible(h).click() for h in hobbies if random.randint(0, 1)]
        self.element_is_visible(self.loc.UPLOAD_PICT).send_keys(file.file_path)
        self.element_is_visible(self.loc.CURRENT_ADDRESS).send_keys(person['address'])
        self.go_to_element(self.element_is_present(self.loc.SELECT_STATE))
        self.element_is_visible(self.loc.SELECT_STATE).click()
        self.element_is_visible(self.loc.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.loc.SELECT_CITY).click()
        self.element_is_visible(self.loc.CITY_INPUT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_present(self.loc.SUBMIT_B))
        self.element_is_visible(self.loc.SUBMIT_B).click()
        file.delete_file()
