# Система управления библиотекой

Это консольное приложение позволяет управлять библиотекой книг. Оно поддерживает добавление, удаление, поиск, отображение и изменение статуса книг.

## Установка и запуск

1. Убедитесь, что у вас установлен Python версии 3.x.
2. Склонируйте репозиторий:
   
   git clone https://github.com/<your_username>/library-management-system.git
   
3. Перейдите в директорию проекта:
   
   cd library-management-system
   
4. Запустите приложение:
   
   python main.py
   

## Функционал

Приложение предлагает следующий набор возможностей:

### Добавление книги
Пользователь вводит название (title), автора (author) и год издания (year), после чего книга добавляется в библиотеку с уникальным идентификатором (id) и статусом «в наличии».

### Удаление книги
Пользователь вводит уникальный идентификатор (id) книги, которую хочет удалить.

### Поиск книги
Пользователь может искать книги по названию (title), автору (author) или году издания (year). Результаты поиска выводятся на экран.

### Отображение всех книг
Приложение выводит список всех книг с их идентификаторами (id), названиями (title), авторами (author), годами издания (year) и статусами (status).

### Изменение статуса книги
Пользователь вводит идентификатор (id) книги и новый статус («в наличии» или «выдана»).

## Структура проекта

- main.py: Основной скрипт, который запускает консольный интерфейс.
- library.py: Модуль, содержащий все функции для работы с библиотекой.
- data.json: Файл для хранения данных о книгах.
- tests.py: Модуль с тестами для проверки основных функций.
- README.md: Этот файл с описанием проекта.

## Примеры использования

Запуск приложения:
python main.py


Интерфейс командной строки:
Добро пожаловать в систему управления библиотекой!

Меню:
1. Добавить книгу
2. Удалить книгу
3. Найти книгу
4. Показать все книги
5. Изменить статус книги
0. Выход


Пример добавления книги:
Выберите пункт меню: 1
Введите название книги: Искусственный интеллект
Введите автора книги: Эндрю Нг
Введите год издания книги: 2023
Книга 'Искусственный интеллект' успешно добавлена.


## Лицензия

Этот проект распространяется под лицензией MIT. Вы можете свободно использовать, изменять и распространять его согласно условиям этой лицензии.
