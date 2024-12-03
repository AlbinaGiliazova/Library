"""Тесты."""

import unittest
from library import Library
import os


class TestLibrary(unittest.TestCase):
    """Тесты библиотеки."""

    def setUp(self):
        """Перед запуском."""
        self.lib = Library()
        self.lib.DATA_FILE = "data_test.json"
        self.lib.save_data([])

    def tearDown(self):
        """После запуска."""
        os.remove(self.lib.DATA_FILE)

    def test_add_book(self):
        """Добавление книги."""
        self.lib.add_book("Книга 1", "Автор 1", "2020")
        books = self.lib.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Книга 1")
        self.assertEqual(books[0].author, "Автор 1")
        self.assertEqual(books[0].year, "2020")
        self.assertEqual(books[0].status, "в наличии")

    def test_delete_book(self):
        """Удаление книги."""
        self.lib.add_book("Книга 1", "Автор 1", "2020")
        self.lib.add_book("Книга 2", "Автор 2", "2019")
        books = self.lib.get_all_books()
        self.assertEqual(len(books), 2)

    def test_search_books_by_title(self):
        """Поиск книг по названию."""
        self.ladd_book("Книга 1", "Автор 1", "2020")
        self.ladd_book("Книга 2", "Автор 2", "2019")
        books = self.lsearch_books("title", "Книга 1")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Книга 1")

    def test_search_books_by_author(self):
        """Поиск книг по автору."""
        self.ladd_book("Книга 1", "Автор 1", "2020")
        self.ladd_book("Книга 2", "Автор 2", "2019")
        books = self.lsearch_books("author", "Автор 1")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["author"], "Автор 1")

    def test_search_books_by_year(self):
        """Поиск книг по году."""
        self.ladd_book("Книга 1", "Автор 1", "2020")
        self.ladd_book("Книга 2", "Автор 2", "2019")
        books = self.lsearch_books("year", "2020")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["year"], "2020")

    def test_change_status(self):
        """Смена статуса."""
        self.ladd_book("Книга 1", "Автор 1", "2020")
        books = self.lget_all_books()
        self.assertEqual(books[0]["status"], "в наличии")

        self.lchange_status(books[0]["id"], "выдана")
        books = self.lget_all_books()
        self.assertEqual(books[0]["status"], "выдана")


if __name__ == '__main__':
    unittest.main()
