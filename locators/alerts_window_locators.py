from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_B = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_B = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE_B = (By.CSS_SELECTOR, '#messageWindowButton')
    ''''''
    TITLE_NEW = (By.CSS_SELECTOR, '#sampleHeading')
