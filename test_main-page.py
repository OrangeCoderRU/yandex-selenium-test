from main_page import MainPage
import pytest
import time

# link = "https://yandex.ru/"

@pytest.mark.parametrize('link', ["https://yandex.ru/"])
def test_search(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()             # открываем страницу
    page.search_request("Поисковый запрос")
    time.sleep(5)
