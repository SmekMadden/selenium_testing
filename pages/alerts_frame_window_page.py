from locators.alerts_window_locators import *
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    loc = BrowserWindowsPageLocators()
    buttons = {'New tab': loc.NEW_TAB_B,
               'New Window': loc.NEW_WINDOW_B,
               'New Window Message': loc.NEW_WINDOW_MESSAGE_B}

    def open_tab(self, tab_name):
        self.element_is_visible(self.buttons[tab_name]).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_new_tab_title(self, title_text):
        text_title = self.element_is_present(self.loc.TITLE_NEW).text
        assert title_text == text_title, 'Title text is not match'


class AlertsPage(BasePage):
    loc = AlertsPageLocators()
    buttons = {'see alert': loc.SEE_ALERT_B,
               'alert will appear': loc.APPEAR_ALERT_APPEAR_AFTER_5_SEC_B,
               'confirm box': loc.CONFIRM_BOX_ALERT_B,
               'prompt box will appear': loc.PROMT_BOX_ALERT_B}

    def get_alert(self):
        return self.driver.switch_to.alert

    def click_button(self, button_name):
        self.element_is_visible(self.buttons[button_name]).click()

    def assert_alert_text(self, text):
        alert_text = self.get_alert().text
        assert alert_text == text, 'text in alert does not match'

    def assert_result_text_for_confirm_box_button(self, text):
        assert text == self.element_is_present(self.loc.CONFIRM_RESULT).text, \
            'Not expected text in the result message'

    def assert_result_text_for_prompt_box_button(self, text):
        assert text == self.element_is_present(self.loc.PROMPT_RESULT).text, \
            'Not expected text in the result message'


class FramesPage(BasePage):
    loc = FramesPageLocators()
    frames = {'frame1': loc.FIRST_FRAME,
              'frame2': loc.SECOND_FRAME
              }

    def get_frame_width_and_height(self, frame_num):
        frame = self.element_is_present(self.frames[frame_num])
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')

        return width, height

    def get_frame_text(self, frame_num):
        frame = self.element_is_present(self.frames[frame_num])
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.loc.TITLE_FRAME).text
        self.driver.switch_to.default_content()

        return text

    @staticmethod
    def assert_frame_text(text, text2):
        assert text == text2, 'Frame text is not equal to expected'

    @staticmethod
    def assert_frame_width_and_height(actual, expected):
        assert actual == expected, \
            'Actual frame height and width are not equal to expected'
