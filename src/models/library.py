"""Модель библиотеки книг"""

import json
from typing import List

from models.book import Book


class Library:
    """Класс библиотеки книг"""

    def __init__(self, storage_file: str = "../data/books.json"):
        self.storage_file = storage_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self) -> None:
        """Загружает книги из файла"""
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                books_data = json.load(f)
                self.books = [Book.from_dict(book) for book in books_data]
        except FileNotFoundError:
            self.books = []

    def save_books(self) -> None:
        """Сохраняет книги в файл"""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            books_data = [book.to_dict() for book in self.books]
            json.dump(books_data, f, ensure_ascii=False, indent=2)

    def add_book(self, book: Book) -> None:
        """Добавляет новую книгу в библиотеку"""
        book.id = self._generate_id()
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id: int) -> bool:
        """Удаляет книгу по ID"""
        initial_length = len(self.books)
        self.books = [book for book in self.books if book.id != book_id]
        if len(self.books) < initial_length:
            self.save_books()
            return True
        return False

    def find_books(self, query: str) -> List[Book]:
        """Поиск книг по названию, автору или году"""
        query = query.lower().strip()
        # Если запрос пустой - возвращаем все книги
        if not query:
            return self.books.copy()

        return [
            book
            for book in self.books
            if query in book.title.lower()
            or query in book.author.lower()
            or query == str(book.year)
        ]

    def get_all_books(self) -> List[Book]:
        """Возвращает список всех книг"""
        return self.books

    def update_status(self, book_id: int, new_status: str) -> bool:
        """Обновляет статус книги"""
        if new_status not in Book.STATUS_CHOICES:
            raise ValueError("Недопустимый статус")

        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return True

        raise KeyError("Книга с указанным ID не найдена")

    def _generate_id(self) -> int:
        """Генерирует уникальный ID для новой книги"""
        return max((book.id for book in self.books), default=0) + 1
