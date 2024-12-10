"""Тесты для библиотеки книг"""

import unittest
import os

from models.book import Book
from models.library import Library


class TestLibrary(unittest.TestCase):
    """Класс тестирования для основных функций библиотеки книг"""

    def setUp(self):
        self.test_file = "test_books.json"
        self.library = Library(storage_file=self.test_file)
        self.test_book = Book(title="Война и мир", author="Толстой", year=1869)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Тест добавления книги в библиотеку"""
        self.library.add_book(self.test_book)
        self.assertEqual(len(self.library.get_all_books()), 1)
        self.assertEqual(self.library.get_all_books()[0].title, "Война и мир")

    def test_remove_book(self):
        """Тест удаления книги из библиотеки"""
        self.library.add_book(self.test_book)
        book_id = self.test_book.id
        self.assertTrue(self.library.remove_book(book_id))
        self.assertEqual(len(self.library.get_all_books()), 0)

    def test_find_books(self):
        """Тест поиска книг в библиотеке"""
        self.library.add_book(self.test_book)
        # Поиск по названию
        found_books = self.library.find_books("Война")
        self.assertEqual(len(found_books), 1)
        # Поиск по автору
        found_books = self.library.find_books("Толстой")
        self.assertEqual(len(found_books), 1)
        # Поиск несуществующей книги
        found_books = self.library.find_books("Гарри Поттер")
        self.assertEqual(len(found_books), 0)

    def test_status_updates(self):
        """Тест обновления статуса книги"""
        self.library.add_book(self.test_book)
        book_id = self.test_book.id

        self.assertTrue(self.library.update_status(book_id, "выдана"))
        self.assertEqual(self.library.get_all_books()[0].status, "выдана")

        self.assertTrue(self.library.update_status(book_id, "в наличии"))
        self.assertEqual(self.library.get_all_books()[0].status, "в наличии")

    def test_invalid_status_update(self):
        """Тест обновления статуса на недопустимое значение"""
        self.library.add_book(self.test_book)
        book_id = self.test_book.id

        with self.assertRaises(ValueError):
            self.library.update_status(book_id, "неправильный статус")

    def test_remove_nonexistent_book(self):
        """Тест удаления несуществующей книги"""
        self.assertFalse(self.library.remove_book(999))

    def test_update_nonexistent_book_status(self):
        """Тест обновления статуса несуществующей книги"""
        with self.assertRaises(KeyError):
            self.library.update_status(999, "выдана")

    def test_find_books_empty_query(self):
        """Тест поиска с пустым запросом"""
        self.library.add_book(self.test_book)
        book2 = Book(title="Евгений Онегин", author="Пушкин", year=1833)
        self.library.add_book(book2)

        # Пустой запрос должен вернуть все книги
        found_books = self.library.find_books("")
        self.assertEqual(len(found_books), 2)

        # Пробелы тоже считаются пустым запросом
        found_books = self.library.find_books("   ")
        self.assertEqual(len(found_books), 2)

    def test_find_books_by_year(self):
        """Тест поиска книг по году"""
        self.library.add_book(self.test_book)
        found_books = self.library.find_books("1869")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].year, 1869)

    def test_unique_book_ids(self):
        """Тест уникальности ID книг"""
        book1 = Book(title="Книга 1", author="Автор", year=2000)
        book2 = Book(title="Книга 2", author="Автор", year=2001)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.assertNotEqual(book1.id, book2.id)

    def test_persistence(self):
        """Тест сохранения и загрузки данных"""
        self.library.add_book(self.test_book)
        original_id = self.test_book.id

        # Создаем новый экземпляр библиотеки с тем же файлом
        new_library = Library(storage_file=self.test_file)
        loaded_books = new_library.get_all_books()

        self.assertEqual(len(loaded_books), 1)
        self.assertEqual(loaded_books[0].id, original_id)
        self.assertEqual(loaded_books[0].title, "Война и мир")
