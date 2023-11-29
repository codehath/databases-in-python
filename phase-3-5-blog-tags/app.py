from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository
from lib.tag_repository import TagRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/student_directory_2.sql")
connection.seed("seeds/blog_posts_tags.sql")


post_repository = PostRepository(connection)

posts = post_repository.find_by_tag(2)
print(posts)


tag_repository = TagRepository(connection)

tags = tag_repository.find_by_post(2)
print(tags)