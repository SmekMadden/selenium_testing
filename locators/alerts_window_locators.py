from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_B = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_B = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE_B = (By.CSS_SELECTOR, '#messageWindowButton')
    ''''''
    TITLE_NEW = (By.CSS_SELECTOR, '#sampleHeading')


class AlertsPageLocators:
    SEE_ALERT_B = (By.CSS_SELECTOR, '#alertButton')
    APPEAR_ALERT_APPEAR_AFTER_5_SEC_B = (By.CSS_SELECTOR, '#timerAlertButton')
    CONFIRM_BOX_ALERT_B = (By.CSS_SELECTOR, '#confirmButton')
    CONFIRM_RESULT = (By.CSS_SELECTOR, '#confirmResult')
    PROMT_BOX_ALERT_B = (By.CSS_SELECTOR, '#promtButton')
    PROMPT_RESULT = (By.CSS_SELECTOR, '#promptResult')
