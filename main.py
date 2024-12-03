"""Основной файл библиотеки."""

import library


def main():
    lib = library.Library()

    print("Добро пожаловать в систему управления библиотекой!")
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            add_book(lib)
        elif choice == '2':
            delete_book(lib)
        elif choice == '3':
            search_books(lib)
        elif choice == '4':
            show_all_books(lib)
        elif choice == '5':
            change_status(lib)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    print("Спасибо за использование нашей системы! До свидания.")


def add_book(lib):
    """Добавление книги."""
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания книги: ")

    try:
        lib.add_book(title, author, year)
        print(f"Книга '{title}' успешно добавлена.")
    except ValueError as e:
        print(e)


def delete_book(lib):
    """Удаление книги."""
    book_id = input("Введите ID книги, которую хотите удалить: ")

    try:
        lib.delete_book(book_id)
        print(f"Книга с ID {book_id} удалена.")
    except ValueError as e:
        print(e)


def search_books(lib):
    """Поиск книг."""
    search_type = input("Что вы хотите найти? (Название, Автор, Год): ").lower()
    search_query = input("Введите запрос: ")

    books = lib.search_books(search_type, search_query)

    if not books:
        print("Книг, соответствующих вашему запросу, не найдено.")
    else:
        for book in books:
            print(f"{book['id']}. {book['title']} ({book['author']}, {book['year']}) - {book['status']}")


def show_all_books(lib):
    """Показ книг."""
    books = lib.get_all_books()

    if not books:
        print("Библиотека пуста.")
    else:
        for book in books:
            print(f"{book.id}. {book.title} ({book.author}, {book.year}) - {book.status}")


def change_status(lib):
    """Смена статуса."""
    book_id = input("Введите ID книги, статус которой хотите изменить: ")
    new_status = input("Введите новый статус ('в наличии' или 'выдана'): ")

    try:
        lib.change_status(book_id, new_status)
        print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
