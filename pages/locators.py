from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_FORM = (By.CSS_SELECTOR, "#text")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search2__button")
