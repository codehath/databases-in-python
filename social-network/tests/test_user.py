from lib.user import User

"""
User constructs with an id, email, and username
"""
def test_user_constructs():
    user = User(1, "test@example.com", "johnsmith")
    assert user.id == 1
    assert user.email == "test@example.com"
    assert user.username == "johnsmith"

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "test@example.com", "johnsmith")
    assert str(user) == "User(1, test@example.com, johnsmith)"

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "test@example.com", "johnsmith")
    user2 = User(1, "test@example.com", "johnsmith")
    assert user1 == user2
