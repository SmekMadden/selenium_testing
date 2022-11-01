import time

from faker import Faker

from pages.alerts_frame_window_page import BrowserWindowPage, AlertsPage, FramesPage


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


class TestAlertsPage:

    def test_see_alert_button(self, driver):
        page = AlertsPage(driver, 'https://demoqa.com./alerts')
        page.open()
        page.click_button('see alert')
        page.assert_alert_text('You clicked a button')

    def test_alert_will_appear_button(self, driver):
        page = AlertsPage(driver, 'https://demoqa.com./alerts')
        page.open()
        page.click_button('alert will appear')
        page.wait_for_alert(6)
        page.assert_alert_text('This alert appeared after 5 seconds')

    def test_confirm_box_button(self, driver):
        page = AlertsPage(driver, 'https://demoqa.com./alerts')
        page.open()
        page.click_button('confirm box')
        page.assert_alert_text('Do you confirm action?')
        page.get_alert().accept()
        page.assert_result_text_for_confirm_box_button('You selected Ok')
        page.click_button('confirm box')
        page.get_alert().dismiss()
        page.assert_result_text_for_confirm_box_button('You selected Cancel')

    def test_prompt_box_button(self, driver):
        page = AlertsPage(driver, 'https://demoqa.com./alerts')
        page.open()
        page.click_button('prompt box will appear')
        page.assert_alert_text('Please enter your name')
        name = Faker('ru_RU').first_name()
        alert = page.get_alert()
        alert.send_keys(name)
        alert.accept()
        page.assert_result_text_for_prompt_box_button(f'You entered {name}')


class TestFramesPage:

    def test_first_frame(self, driver):
        page = FramesPage(driver, 'https://demoqa.com./frames')
        page.open()
        text = page.get_frame_text('frame1')
        width_height = page.get_frame_width_and_height('frame1')
        page.assert_frame_text(text, 'This is a sample page')
        page.assert_frame_width_and_height(width_height, ('500px', '350px'))

    def test_second_frame(self, driver):
        page = FramesPage(driver, 'https://demoqa.com./frames')
        page.open()
        text = page.get_frame_text('frame2')
        width_height = page.get_frame_width_and_height('frame2')
        page.assert_frame_text(text, 'This is a sample page')
        page.assert_frame_width_and_height(width_height, ('100px', '100px'))
