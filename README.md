# Library Test Task

A simple console-based library management system written in Python that allows you to manage books in a library.

## Features

-   Add new books with title, author, and year
-   Remove books by ID
-   Search books by title, author, or year
-   Display all books in the library
-   Update book status (available/borrowed)
-   Persistent storage using JSON

## Requirements

-   Python 3.12+
-   Docker (optional)
-   Docker Compose (optional)

## Installation

1. Clone the repository:
   git clone <https://github.com/w1sq/library-test-task.git>
   cd library-test-task

2. Using Docker (recommended):
   docker-compose build
   docker-compose run --rm library

3. Without Docker:
   cd src
   python3 main.py

## Running Tests

With Docker:
docker-compose run --rm tests

Without Docker:
cd src
python -m unittest tests/test_library.py

## Project Structure

.
├── docker/
│ ├── Dockerfile
│ └── Dockerfile.test
├── src/
│ ├── models/
│ │ ├── book.py
│ │ └── library.py
│ ├── tests/
│ │ └── test_library.py
│ └── main.py
├── data/
│ └── books.json
├── docker-compose.yml
└── README.md

## Usage

The application provides a console interface with the following options:

1. Add a book
2. Remove a book
3. Find a book
4. Show all books
5. Change book status
6. Exit

## Book Status

Books can have two statuses:

-   в наличии (available)
-   выдана (borrowed)

## Development

The project uses:

-   Python dataclasses for models
-   JSON for data persistence
-   unittest for testing
-   Docker for containerization

## Testing

The test suite includes tests for:

-   Book addition and removal
-   Book search functionality
-   Status updates
-   Data persistence
-   Edge cases and error handling
-   ETC

## Docker Support

The project includes two Dockerfile configurations:

-   Dockerfile - for running the application
-   Dockerfile.test - for running tests
