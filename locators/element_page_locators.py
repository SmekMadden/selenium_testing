from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # fields form
    FULL_NAME = (By.CSS_SELECTOR, "#userName")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#permanentAddress")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")

    OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERM_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    CHECKBOX_LIST = (By.CSS_SELECTOR, 'span.rct-text')
    CHECKED_BOXES = (By.CSS_SELECTOR, '.rct-icon-check')
    RESULT_MESSAGE = (By.CSS_SELECTOR, '#result')
    BOX_NAMES_FROM_RESULT = (By.CSS_SELECTOR, 'span.text-success')
    CHECKBOX_TITLE = (By.XPATH, './/ancestor::span[@class="rct-text"]')
