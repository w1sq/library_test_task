"""Основной модуль для запуска консольного приложения"""

from models.book import Book
from models.library import Library


def print_menu():
    """Функция вывода меню"""
    print("\n=== Меню Библиотеки ===")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("0. Выход")


def main():
    """Основная функция запуска консольного приложения"""
    library = Library()

    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            try:
                year = int(input("Введите год издания: ").strip())
                book = Book(title=title, author=author, year=year)
                library.add_book(book)
                print("Книга успешно добавлена!")
            except ValueError:
                print("Ошибка: год должен быть числом")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: ").strip())
                if library.remove_book(book_id):
                    print("Книга успешно удалена!")
                else:
                    print("Книга с указанным ID не найдена")
            except ValueError:
                print("Ошибка: ID должен быть числом")

        elif choice == "3":
            query = input("Введите поисковый запрос: ").strip()
            books = library.find_books(query)
            if books:
                print("\nНайденные книги:")
                for book in books:
                    print(book)
            else:
                print("Книги не найдены")

        elif choice == "4":
            books = library.get_all_books()
            if books:
                print("\nСписок всех книг:")
                for book in books:
                    print(book)
            else:
                print("Библиотека пуста")

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: ").strip())
                status = input("Введите новый статус (в наличии/выдана): ").strip()
                library.update_status(book_id, status.lower())
                print("Статус книги успешно обновлен!")
            except ValueError as e:
                if str(e) == "Недопустимый статус":
                    print(
                        "Ошибка: недопустимый статус. Используйте 'в наличии' или 'выдана'"
                    )
                else:
                    print("Ошибка: ID должен быть числом")
            except KeyError:
                print("Ошибка: книга с указанным ID не найдена")

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
