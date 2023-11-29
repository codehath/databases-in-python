from lib.item import item
from lib.item_repository import itemRepository

"""
all returns all records from table
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/item_directory_2.sql")
    item_repository = itemRepository(db_connection)
    assert item_repository.all() == [
                item(1, 'Dan', 1),
                item(2, 'John', 1),
                item(3, 'James', 1),
                item(4, 'Annabel', 1),
                item(5, 'Sarah', 2),
                item(6, 'Holly', 2),
                item(7, 'Amber', 2),
                item(8, 'George', 3),
                item(9, 'Jamie', 3),
                item(10, 'Josh', 3)
    ]
