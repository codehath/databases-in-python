from lib.database_connection import DatabaseConnection
from lib.item import Item
from lib.order import Order
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository

class Application():
    def __init__(self):
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()

        # Seed with some seed data
        self._connection.seed("seeds/shop_manager.sql")

    def run(self):
        item_repository = ItemRepository(self._connection)
        order_repository = OrderRepository(self._connection)

        print("Welcome to the shop management program!")
        print("What do you want to do?")
        print(" 1 = list all shop items")
        print(" 2 = create a new item")
        print(" 3 = list all orders")
        print(" 4 = create a new order")
        print(" 5 = Find items by order")
        print("Enter your choice: ")
        choice = input()
        if choice == "1":
            self.print_all_items(item_repository)

        elif choice == "2":
            # Retrieve all items
            item_repository.create(Item(None, 'Infinite Pizza Maker', 149.95, 10))
            print("Item added")
            self.print_all_items(item_repository)

        elif choice == "3":
            self.print_all_orders(order_repository)

        elif choice == "4":
            all_items = item_repository.all()
            # Create new order
            items_quantities = {all_items[2]:3, all_items[0]:1, all_items[4]:2, all_items[8]:4}
            order_repository.create(Order(None, "Jack Black", '2023-11-30'), items_quantities)

            print("Order added.")
            self.print_all_orders(order_repository)
            
        elif choice == "5":
            # Retrieve order 3
            order = order_repository.find_order_by_id(3)
            print(order)
    
    def print_all_items(self, item_repository):
        # Retrieve all items
        items = item_repository.all()

        print("Here is a list of items:")
        # List them out
        for item in items:
            print(item)

    def print_all_orders(self, order_repository):
        # Retrieve all orders
        orders = order_repository.all_with_items()

        print("Here is a list of orders:")
        # List them out
        for order in orders:
            print(order)

if __name__ == '__main__':
    app = Application()
    app.run()