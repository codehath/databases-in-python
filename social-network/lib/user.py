class User:
    # We initialize with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, email, username):
        self.id = id
        self.email = email
        self.username = username

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print a User
    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.username})"
