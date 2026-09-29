\# Документация интеграции



\## Архитектура взаимодействия

Система состоит из 4 модулей:

1\. `input\_module.py` — ввод данных, сохранение в data\_input.json

2\. `process\_module.py` — чтение JSON, обработка, сохранение в data\_output.json

3\. `output\_module.py` — чтение JSON, вывод на экран

4\. `main.py` — оркестратор (вызывает все модули по очереди)



\## Схема потоков данных

Пользователь → input\_module → data\_input.json → process\_module → data\_output.json → output\_module → Экран



\## Формат обмена

JSON-файлы. Пример data\_input.json:

{

&#x20; "n": 2, "m": 3,

&#x20; "matrix": \[\[1.5, 2.5, 3.5], \[4.5, 5.5, 6.5]]

}



\## Пример ответа (data\_output.json):

{

&#x20; "n": 2, "m": 3,

&#x20; "result\_matrix": \[\[1.5, 4.5], \[2.5, 5.5], \[3.5, 6.5]]

}

