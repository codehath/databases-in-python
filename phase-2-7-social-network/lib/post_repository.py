from lib.post import Post

class PostRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all posts
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["user_id"], row["title"], row["content"], row["views"])
            posts.append(item)
        return posts

    # Find a single post by its id
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * FROM posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["user_id"], row["title"], row["content"], row["views"])

    # Create a new post
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, post):
        self._connection.execute('INSERT INTO posts (user_id, title, content, views) VALUES (%s, %s, %s, %s)', [
                                 post.user_id, post.title, post.content, post.views])
        return None

    # Delete a post by its id
    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None
