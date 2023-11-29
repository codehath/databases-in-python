from lib.comment import Comment

"""
constructs with values
"""

def test_constructs_with_values():
    comment = Comment(1, 'Great post!', 1, 'Emily Johnson')
    assert comment.id == 1
    assert comment.content == 'Great post!'
    assert comment.post_id == 1
    assert comment.user == 'Emily Johnson'

"""
has string representation
"""

def test_string_representation():
    comment = Comment(1, 'Great post!', 1, 'Emily Johnson')
    assert str(comment) == "Comment(1, Great post!, Post ID: 1, Emily Johnson)"

"""
instances with same values are equal
"""

def test_instances_same_value_are_equal():
    comment1 = Comment(1, 'Great post!', 1, 'Emily Johnson')
    comment2 = Comment(1, 'Great post!', 1, 'Emily Johnson')
    assert comment1 == comment2