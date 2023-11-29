from lib.item import Item

"""
constructs with values
"""

def test_constructs_with_values():
    item = Item(1, 'name', 1)
    assert item.id == 1
    assert item.name == 'name'
    assert item.order_id == 1

"""
has string representation
"""

def test_string_representation():
    item = Item(1, 'name', 1)
    assert str(item) == f"item({1}, {'name'}, {1})"

"""
instanes with same values are equal
"""

def test_instances_same_value_are_equal():
    item1 = Item(1, 'name', 1)
    item2 = Item(1, 'name', 1)
    assert item1 == item2
