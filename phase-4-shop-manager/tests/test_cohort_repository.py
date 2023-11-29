from lib.order import Order
from lib.order_repository import OrderRepository
from lib.item import item
"""
#all returns all records
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/item_directory_2.sql")
    order_repository = OrderRepository(db_connection)
    assert order_repository.all() == [
        Order(1, 'apprenticeship', '2023-10-30'),
        Order(2, 'main bootcamp', '2023-10-30'),
        Order(3, 'DfE,', '2023-10-30')
    ]

def test_find_order_with_items(db_connection):
    db_connection.seed("seeds/item_directory_2.sql")
    order_repository = OrderRepository(db_connection)
    assert order_repository.find_order_with_items(3) == Order(3, 'DfE,', '2023-10-30', [
            item(8, 'George', 3),
            item(9, 'Jamie', 3),
            item(10, 'Josh', 3)
        ])



