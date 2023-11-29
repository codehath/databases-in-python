from lib.post import Post
from lib.tag import Tag

class PostRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM posts')
        posts = [
            Post(row['id'], row['title']) for row in rows
            ]
        return posts
    
    # def find_post_with_tags(self, post_id):
    #     rows = self.connection.execute(
    #         "SELECT posts.id AS post_id, posts.title, tags.id AS tag_id, tags.name " \
    #         "FROM posts JOIN tags ON tags.post_id = posts.id " \
    #         'WHERE posts.id = %s', [post_id])
    #     tags = []
    #     for row in rows:
    #         tag = tag(row['tag_id'], row['content'], row['user'], row['post_id'])
    #         tags.append(tag)
        
    #     return Post(rows[0]['post_id'], rows[0]['title'], rows[0]['content'], tags)
    

    def find_by_tag(self, tag_id):
        rows = self.connection.execute(
            "SELECT posts.id, posts.title " \
            "FROM posts " \
            "JOIN posts_tags ON posts_tags.post_id = posts.id " \
            "JOIN tags ON posts_tags.tag_id = tags.id " \
            "WHERE tags.id = %s", [tag_id])
        posts = []
        for row in rows:
            post = Post(row['id'], row['title'])
            posts.append(post)
        
        return posts
    


