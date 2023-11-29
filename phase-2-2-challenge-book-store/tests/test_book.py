from lib.book import Book

"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, "Test Book", "John Smith")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "John Smith"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test Book", "John Smith")
    assert str(book) == "Book(1, Test Book, John Smith)"

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test Book", "John Smith")
    book2 = Book(1, "Test Book", "John Smith")
    assert book1 == book2
