import math
import time
from selenium.common.exceptions import NoAlertPresentException

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
