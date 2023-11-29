class Post:
    def __init__(self, id, user_id, title, content, views):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.content = content
        self.views = views

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Post(Post ID: {self.id}, User ID: {self.user_id}, {self.title}, {self.content}, {self.views} Views)"