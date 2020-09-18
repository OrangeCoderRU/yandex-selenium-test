# yandex-selenium-test

###  Test case №1

### Тест поиска

`test_main-page.py/test_search()`

| № | Шаг | Function | Ожидаемый результат | Фактический результат |
| --- | --- | --- | --- | --- |
| 1 | Открыть страницу yandex.ru | `page.open()` | Открылся браузер со страницей Яндекса | OK |
| 2 | В форму поиска ввести "Поисковый запрос" и нажать "найти" | `page.search_request("Поисковый запрос")` | Открылась страница с поисковой выдачей введенного запроса | OK |
| 3 | Вернуться на главную страницу нажатием на Лого Яндекса | `page.back_to_main()` | Открылась главная страница Яндекса | OK |
| 4 | Тест завершает работу закрытием браузера | *конфиг закрывает браузер автоматически* | Браузер закрылся | OK |
