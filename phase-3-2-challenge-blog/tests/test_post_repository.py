from lib.post import Post
from lib.post_repository import PostRepository
from lib.comment import Comment
"""
#all returns all records
"""

def test_returns_all(db_connection):
    db_connection.seed("seeds/blog_directory.sql")
    post_repository = PostRepository(db_connection)
    assert post_repository.all() == [
        Post(1, 'First Post', 'This is the content of the first post.'),
        Post(2, 'Programming Tips', 'Here are some tips for programming.'),
        Post(3, 'Travel Adventures', 'Exploring new places and cultures.')
    ]

def test_find_post_with_comments(db_connection):
    db_connection.seed("seeds/blog_directory.sql")
    post_repository = PostRepository(db_connection)
    print(post_repository.find_post_with_comments(3))
    assert post_repository.find_post_with_comments(3) == Post(3, 'Travel Adventures', 'Exploring new places and cultures.', [
            Comment(5, 'What an exciting travel experience!', 3, 'Olivia Wilson'),
            Comment(8, 'Can you share more details about your travel?', 3, 'Noah Smith'),
            Comment(10, 'Looking forward to more travel stories.', 3, 'Mason Taylor')
        ])