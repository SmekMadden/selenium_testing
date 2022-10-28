from pages.alerts_frame_window_page import BrowserWindowPage


class TestBrowserWindow:
    pass

    def test_new_tab(self, driver):
        page = BrowserWindowPage(driver, 'https://demoqa.com./browser-windows')
        page.open()
        page.open_tab('New tab')
        page.assert_new_tab_title('This is a sample page')

    def test_new_window_tab(self, driver):
        page = BrowserWindowPage(driver, 'https://demoqa.com./browser-windows')
        page.open()
        page.open_tab('New Window')
        page.assert_new_tab_title('This is a sample page')
