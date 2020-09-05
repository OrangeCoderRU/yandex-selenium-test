from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def search_request(self, string):
        search_form = self.browser.find_element(*MainPageLocators.SEARCH_FORM)
        search_form.send_keys(string)
        search_button = self.browser.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
