import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
