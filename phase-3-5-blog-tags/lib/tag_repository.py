from lib.tag import Tag
from lib.tag import Tag

class TagRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM tags')
        tags = [
            Tag(row['id'], row['name']) for row in rows
            ]
        return tags
    
    # def find_tag_with_tags(self, tag_id):
    #     rows = self.connection.execute(
    #         "SELECT tags.id AS tag_id, tags.title, tags.id AS tag_id, tags.name " \
    #         "FROM tags JOIN tags ON tags.tag_id = tags.id " \
    #         'WHERE tags.id = %s', [tag_id])
    #     tags = []
    #     for row in rows:
    #         tag = tag(row['tag_id'], row['content'], row['user'], row['tag_id'])
    #         tags.append(tag)
        
    #     return Tag(rows[0]['tag_id'], rows[0]['title'], rows[0]['content'], tags)
    

    def find_by_post(self, post_id):    
        rows = self.connection.execute(
            "SELECT tags.id, tags.name FROM tags " \
            "JOIN posts_tags ON posts_tags.tag_id = tags.id " \
            "JOIN posts ON posts_tags.post_id = posts.id " \
            "WHERE posts.id = %s", [post_id])
        
        tags = [Tag({row['id']}, {row['name']}) for row in rows]
    
        return tags


