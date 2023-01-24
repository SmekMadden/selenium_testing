from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, '#section1Heading')
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, '#section1Content p')

    SECOND_SECTION = (By.CSS_SELECTOR, '#section2Heading')
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, '#section2Content p')

    THIRD_SECTION = (By.CSS_SELECTOR, '#section3Heading')
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, '#section3Content p')


class AutoCompletePageLocators:
    MULTI_FIELD = (By.CSS_SELECTOR, '#autoCompleteMultipleInput')
    SINGLE_FIELD = (By.CSS_SELECTOR, '#autoCompleteSingleInput')
    MULTI_REMOVE = (By.CSS_SELECTOR, '.auto-complete__multi-value__remove svg path')
