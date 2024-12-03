"""Основные классы библиотеки."""

import json
from uuid import uuid4


class Book:
    """Класс, представляющий книгу."""

    def __init__(self,
                 title: str,
                 author: str,
                 year: int,
                 status: str = "в наличии"):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Преобразование объекта книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    """Класс, представляющий библиотеку книг."""
    DATA_FILE = "data.json"

    def __init__(self):
        self.books = self.load_data()

    def load_data(self):
        """Загрузка данных из файла."""
        try:
            with open(Library.DATA_FILE, "r", encoding="UTF-8") as file:
                return [Book(**book) for book in json.load(file)]
        except FileNotFoundError:
            return []

    def save_data(self):
        """Сохранение данных в файл."""
        with open(Library.DATA_FILE, "w", encoding="UTF-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self,
                 title: str,
                 author: str,
                 year: int):
        """Добавление новой книги в библиотеку."""
        # Проверка на существование книги с таким же названием и автором
        existing_book = next((b for b in self.books if b.title == title and b.author == author), None)
        if existing_book:
            raise ValueError(f"Книга '{title}' от автора '{author}' уже существует.")

        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_data()

    def delete_book(self,
                    book_id: int):
        """Удаление книги из библиотеки."""
        found = False
        for i, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[i]
                found = True
                break

        if not found:
            raise ValueError(f"Книга с ID {book_id} не найдена.")

        self.save_data()

    def search_books(self,
                     search_type: str,
                     query: str):
        """Поиск книг по названию, автору или году."""
        results = []
        for book in self.books:
            if search_type == "title":
                if query.lower() in book.title.lower():
                    results.append(book)
            elif search_type == "author":
                if query.lower() in book.author.lower():
                    results.append(book)
            elif search_type == "year":
                if query == book.year:
                    results.append(book)

        return results

    def get_all_books(self):
        """Получение списка всех книг."""
        return self.books

    def change_status(self,
                      book_id: int,
                      new_status: str):
        """Изменение статуса книги."""
        valid_statuses = ["в наличии", "выдана"]
        if new_status not in valid_statuses:
            raise ValueError(f"Недопустимый статус '{new_status}'. Допустимые значения: {', '.join(valid_statuses)}.")

        found = False
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                found = True
                break

        if not found:
            raise ValueError(f"Книга с ID {book_id} не найдена.")

        self.save_data()


if __name__ == "__main__":
    my_library = Library()
    my_library.add_book("Книга 1", "Автор 1", "2020")
    my_library.add_book("Книга 2", "Автор 2", "2019")
    print(my_library.get_all_books())
