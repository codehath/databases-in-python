from lib.post import Post
from lib.comment import Comment

class PostRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        posts = [
            Post(row['id'], row['title'], row['content']) for row in rows
            ]
        return posts
    
    def find_post_with_comments(self, post_id):
        rows = self.connection.execute(
            "SELECT posts.id AS post_id, posts.title, posts.content, comments.id AS comment_id, comments.content as comment, comments.post_id, comments.user " \
            "FROM posts JOIN comments ON comments.post_id = posts.id " \
            'WHERE posts.id = %s', [post_id])
        comments = []
        for row in rows:
            comment = Comment(row['comment_id'], row['comment'], row['post_id'], row['user'])
            comments.append(comment)
        
        return Post(rows[0]['post_id'], rows[0]['title'], rows[0]['content'], comments)
