import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def switch_to_the_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_the_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def assert_status_code(self, url, valid_status_code):
        r = requests.get(url)
        if isinstance(valid_status_code, list):
            assert r.status_code in valid_status_code, 'Status code is not equal to expected'
        else:
            assert r.status_code == valid_status_code, 'Status code is not equal to expected'
        return self

    def wait_for_alert(self, timeout=2):
        Wait(self.driver, timeout).until(EC.alert_is_present())
