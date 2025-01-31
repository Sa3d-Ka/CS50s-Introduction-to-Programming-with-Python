import pytest
from project import AddBook, UpdateBook, DeleteBook, SearchBookByTitle, books


def test_AddBook():
    # Test adding a new book
    result = AddBook("test title", "test author")
    assert result == "The book 'Test Title' was added successfully."
    assert "test title" in books

    # Test adding a duplicate book
    result = AddBook("test title", "test author")
    assert result == "This book already exists."

def test_UpdateBook():
    # Add a book to update
    books["test title"] = "test author"

    # Test updating the title
    result = UpdateBook("test title", new_title="new title")
    assert result == "The book 'Test Title' was updated to 'New Title' successfully."
    assert "new title" in books
    assert "test title" not in books

    # Test updating the author
    result = UpdateBook("new title", new_author="new author")
    assert result == "The author of 'New Title' was updated to 'New Author' successfully."
    assert books["new title"] == "new author"

def test_DeleteBook():
    # Add a book to delete
    books["test title"] = "test author"

    # Test deleting the book
    result = DeleteBook("test title")
    assert result == "The book 'Test Title' was deleted successfully."
    assert "test title" not in books

    # Test deleting a non-existent book
    result = DeleteBook("non-existent title")
    assert result == "This book does not exist."

def test_SearchBookByTitle():
    # Add a book to search
    books["test title"] = "test author"

    # Test searching for an existing book
    result = SearchBookByTitle("test title")
    assert result == {"title": "test title", "author": "test author"}

    # Test searching for a non-existent book
    result = SearchBookByTitle("non-existent title")
    assert result is None

if __name__ == "__main__":
    pytest.main()