from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network_tables.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() # Get all posts

    # Assert on the results
    assert posts == [
        Post(1, 1, 'First Post', 'This is the content of the first post.', 15),
        Post(2, 2, 'Hello World', 'Just saying hello to the world!', 8),
        Post(3, 1, 'Travel Adventures', 'Exploring new places and making memories.', 22),
        Post(4, 3, 'Tech News', 'Latest updates in the tech world.', 10),
        Post(5, 2, 'Favorite Users', 'A list of my favorite users and why I love them.', 18)
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network_tables.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, 1, 'Travel Adventures', 'Exploring new places and making memories.', 22)

"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network_tables.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 2, 'New Post', 'Brand new content for the new post.', 5))

    result = repository.all()
    assert result == [
        Post(1, 1, 'First Post', 'This is the content of the first post.', 15),
        Post(2, 2, 'Hello World', 'Just saying hello to the world!', 8),
        Post(3, 1, 'Travel Adventures', 'Exploring new places and making memories.', 22),
        Post(4, 3, 'Tech News', 'Latest updates in the tech world.', 10),
        Post(5, 2, 'Favorite Users', 'A list of my favorite users and why I love them.', 18),
        Post(6, 2, 'New Post', 'Brand new content for the new post.', 5)
    ]

"""
When we call PostRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network_tables.sql")
    repository = PostRepository(db_connection)
    repository.delete(3)

    result = repository.all()
    assert result == [
        Post(1, 1, 'First Post', 'This is the content of the first post.', 15),
        Post(2, 2, 'Hello World', 'Just saying hello to the world!', 8),
        Post(4, 3, 'Tech News', 'Latest updates in the tech world.', 10),
        Post(5, 2, 'Favorite Users', 'A list of my favorite users and why I love them.', 18)
    ]
