from lib.book_repository import BookRepository
from lib.book import Book

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new BookRepository

    books = repository.all() # Get all books

    # Assert on the results
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
    ]

# """
# When we call BookRepository#find
# We get a single Book object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = BookRepository(db_connection)

#     book = repository.find(3)
#     assert book == Book(3, "Taylor Swift", "Pop")

# """
# When we call BookRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = BookRepository(db_connection)

#     repository.create(Book(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Book(1, "Pixies", "Rock"),
#         Book(2, "ABBA", "Pop"),
#         Book(3, "Taylor Swift", "Pop"),
#         Book(4, "Nina Simone", "Jazz"),
#         Book(5, "The Beatles", "Rock"),
#     ]

# """
# When we call BookRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = BookRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Book(1, "Pixies", "Rock"),
#         Book(2, "ABBA", "Pop"),
#         Book(4, "Nina Simone", "Jazz"),
#     ]
