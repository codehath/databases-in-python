from lib.item import Item
from lib.item import Item

class ItemRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM items')
        items = [
            Item(row['id'], row['name'], row['price'], row['quantity']) for row in rows
            ]
        return items
    
    # def find_item_with_items(self, item_id):
    #     rows = self.connection.execute(
    #         "SELECT items.id AS item_id, items.title, items.id AS item_id, items.name " \
    #         "FROM items JOIN items ON items.item_id = items.id " \
    #         'WHERE items.id = %s', [item_id])
    #     items = []
    #     for row in rows:
    #         item = item(row['item_id'], row['content'], row['user'], row['item_id'])
    #         items.append(item)
        
    #     return Item(rows[0]['item_id'], rows[0]['title'], rows[0]['content'], items)
    
    
    def create(self, item):
        self.connection.execute('INSERT INTO items (name, price, quantity) VALUES (%s, %s, %s)', [
                                 item.name, item.price, item.quantity])
        return None

    def find_by_order(self, order_id):    
        rows = self.connection.execute(
            "SELECT items.id, items.name FROM items " \
            "JOIN orders_items ON orders_items.item_id = items.id " \
            "JOIN orders ON orders_items.order_id = orders.id " \
            "WHERE orders.id = %s", [order_id])
        
        items = [Item({row['id']}, {row['name']}) for row in rows]
    
        return items


