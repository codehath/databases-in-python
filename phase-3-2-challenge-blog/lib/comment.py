class Comment:
    
    def __init__(self, id, content, post_id, user):
        self.id = id
        self.content = content
        self.post_id = post_id
        self.user = user

    def __repr__(self):
        return f"Comment({self.id}, {self.content}, Post ID: {self.post_id}, {self.user})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__