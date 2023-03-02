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


class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, '#frame1')
    SECOND_FRAME = (By.CSS_SELECTOR, '#frame2')
    TITLE_FRAME = (By.CSS_SELECTOR, '#sampleHeading')


class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, '#frame1')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'body > iframe')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, '#showSmallModal')
    SMALL_MODAL_TITLE = (By.CSS_SELECTOR, '#example-modal-sizes-title-sm')
    SMALL_MODAL_BODY = (By.CSS_SELECTOR, 'div.modal-body')
    SMALL_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '#closeSmallModal')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, '#showLargeModal')
    LARGE_MODAL_TITLE = (By.CSS_SELECTOR, '#example-modal-sizes-title-lg')
    LARGE_MODAL_BODY = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    LARGE_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '#closeLargeModal')
