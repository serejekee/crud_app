# ToDo Python Project with PostgreSQL
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue?style=for-the-badge&logo=postgresql)

Это простой проект на Python, который реализует базовые операции с базой данных PostgreSQL для управления задачами (ToDo). В проекте используются основные CRUD-операции: создание, чтение, обновление и удаление задач.

## Структура проекта

```bash
├── db.py # Подключение и инициализация БД
├── todo.py # CRUD-операции
└── main.py # Тестирование функций
```


## Требования

- Python 3.x
- PostgreSQL
- Библиотека `psycopg2` для работы с PostgreSQL

## Установка

1. Создаем базу данных:
```bash
createdb todo_db
```

2. Установите необходимые зависимости:
```bash
pip install psycopg2-binary
```
3. Обновляем параметры подключения в файле db.py:
```bash
def get_connection():
    return psycopg2.connect(
        dbname="todo_db",    # Имя вашей базы данных
        user="postgres",     # Ваш PostgreSQL user
        password="yourpassword",  # Ваш пароль
        host="localhost",    # Адрес сервера PostgreSQL
        port="5432"          # Порт (по умолчанию 5432)
    )
```
## Как использовать
1. Для инициализации базы данных и создания таблицы, запустите файл db.py (эта операция будет выполнена автоматически при запуске основного скрипта main.py):
```bash
python db.py
```
2. Запустите основной скрипт main.py, чтобы протестировать работу CRUD-операций:
```bash
python main.py
```
3. Скрипт создаст несколько задач, отобразит их, пометит одну как завершённую и удалит другую. Вывод будет выглядеть примерно так:
```python
Список задач:
(1, 'Купить молоко', False)
(2, 'Сделать домашку', False)

После обновлений:
(1, 'Купить молоко', True)
```
## Описание файлов
- db.py: Содержит функции для подключения к базе данных и создания таблицы.
- todo.py: Содержит функции для добавления, вывода, обновления и удаления задач.
- main.py: Пример использования функций для тестирования CRUD-операций.

## 📝 Лицензия
[MIT License](LICENSE) — бесплатно для использования,адаптируй, и изменяй 🤘
