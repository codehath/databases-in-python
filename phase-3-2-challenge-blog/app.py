from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/student_directory_2.sql")
connection.seed("seeds/blog_directory.sql")


post_repository = PostRepository(connection)

post = post_repository.find_post_with_comments(1)
print(post)