from selenium.webdriver.common.by import By


class RegistrationFormLocators:
    FIRSTNAME = (By.CSS_SELECTOR, '#firstName')
    LASTNAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    MALE_RB = (By.CSS_SELECTOR, '#genterWrapper .col-md-9 div:nth-child(1)')
    FEMALE_RB = (By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[2]')
    OTHER_RB = (By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[3]')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    BIRTHDAY = (By.CSS_SELECTOR, '#dateOfBirthInput')
    SUBJECTS = (By.CSS_SELECTOR, '#subjectsInput')
    SPORT_B = (By.XPATH, '//div[@id="hobbiesWrapper"]/div[2]/div[1]')
    READING_B = (By.XPATH, '//div[@id="hobbiesWrapper"]/div[2]/div[2]')
    MUSIC_B = (By.XPATH, '//div[@id="hobbiesWrapper"]/div[2]/div[3]')
    UPLOAD_PICT = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    SELECT_STATE = (By.CSS_SELECTOR, '#state')
    STATE_INPUT = (By.CSS_SELECTOR, '#react-select-3-input')
    SELECT_CITY = (By.CSS_SELECTOR, '#city')
    CITY_INPUT = (By.CSS_SELECTOR, '#react-select-4-input')
    SUBMIT_B = (By.CSS_SELECTOR, '#submit')
