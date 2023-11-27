from lib.post import Post

"""
Post constructs with an id, user_id, title, content, and views
"""
def test_post_constructs():
    post = Post(1, 1, 'First Post', 'This is the content of the first post.', 15)
    assert post.id == 1
    assert post.user_id == 1
    assert post.title == 'First Post'
    assert post.content == 'This is the content of the first post.'
    assert post.views == 15

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, 1, 'First Post', 'This is the content of the first post.', 15)
    assert str(post) == "Post(Post ID: 1, User ID: 1, First Post, This is the content of the first post., 15 Views)"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, 1, 'First Post', 'This is the content of the first post.', 15)
    post2 = Post(1, 1, 'First Post', 'This is the content of the first post.', 15)
    assert post1 == post2