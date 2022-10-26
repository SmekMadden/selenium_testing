import locators.alerts_window_locators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    loc = locators.allerts_window_locators.BrowserWindowsPageLocators
    buttons = {'New tab': loc.NEW_TAB_B, 'New Window': loc.NEW_WINDOW_B,
               'New Window Message': loc.NEW_WINDOW_MESSAGE_B}

    def open_tab(self, tab_name):
        self.element_is_visible(self.buttons[tab_name]).click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def assert_new_tab_title(self, title_text):
        text_title = self.element_is_present(self.loc.TITLE_NEW).text
        assert title_text == text_title, 'Title text is not match'
