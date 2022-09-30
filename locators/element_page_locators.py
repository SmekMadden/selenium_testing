from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # fields form
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
