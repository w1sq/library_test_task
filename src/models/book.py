"""Модель книги"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Book:
    """Класс книги"""

    STATUS_CHOICES = ["в наличии", "выдана"]

    title: str
    author: str
    year: int
    status: str = "в наличии"
    id: Optional[int] = None

    def __str__(self):
        return (
            f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, "
            f"Год: {self.year}, Статус: {self.status}"
        )

    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь для сохранения"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """Создает объект книги из словаря"""
        return Book(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )
