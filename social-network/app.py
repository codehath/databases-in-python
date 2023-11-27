from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/user_store.sql")

# Retrieve all users
user_repository = UserRepository(connection)
users = user_repository.all()

# List them out
for user in users:
    print(user)