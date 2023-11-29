from lib.order import Order
from lib.item import Item

class OrderRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM orders')
        orders = [
            Order(row['id'], row['customer_name'], row['order_date']) for row in rows
            ]
        
        return orders
    
    def all_with_items(self, id_of_order = None):
        command = "SELECT orders.id AS order_id, orders.customer_name, orders.order_date, items.id AS item_id, items.name as item, items.price, orders_items.quantity " \
                "FROM orders " \
                "JOIN orders_items ON orders_items.order_id = orders.id " \
                "JOIN items ON orders_items.item_id = items.id "
        
        params = None
        if id_of_order != None:
            command += 'WHERE orders.id = %s'
            params = [id_of_order]

        rows = self.connection.execute(command, params)

        orders = []
        order_id = None
        for row in rows:
            if row['order_id'] != order_id:
                orders.append(Order(row['order_id'], row['customer_name'], row['order_date'], []))
                order_id = row['order_id']

            item = Item(row['item_id'], row['item'], row['price'], row['quantity'])
            orders[-1].items.append(item)
        
        return orders


    def find_order_by_id(self, order_id):
        return self.all_with_items(order_id)[0]
    

    def find_by_item(self, item_id):
        rows = self.connection.execute(
            "SELECT orders.id, orders.customer_name, orders_order_date, orders_items.quantity " \
            "FROM orders " \
            "JOIN orders_items ON orders_items.order_id = orders.id " \
            "JOIN items ON orders_items.item_id = items.id " \
            "WHERE items.id = %s", [item_id])
        orders = []
        for row in rows:
            order = Order(row['id'], row['customer_name'], row['order_date'])
            orders.append(order)
        
        return orders
    

    def create(self, order, items_quantities):
        order_id = self.connection.execute('INSERT INTO orders (customer_name, order_date) VALUES (%s, %s) RETURNING id', [
                                 order.customer_name, order.order_date])
        for item, quantity in items_quantities.items():
            self.connection.execute('INSERT INTO orders_items (order_id, item_id, quantity) VALUES (%s, %s, %s)', [
                                 order_id[0]["id"], item.id, quantity])
        return None
