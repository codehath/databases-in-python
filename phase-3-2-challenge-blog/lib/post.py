class Post:
    def __init__(self, id, title, content, comments=[]):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.comments})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
