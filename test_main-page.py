from pages.main_page import MainPage
import pytest
import time


@pytest.mark.parametrize('link', ["https://yandex.ru/"])
def test_search(browser, link):
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()             # открываем страницу
    page.search_request("Поисковый запрос")
    time.sleep(2)
    page.back_to_main()
    time.sleep(2)
