from lib.order import Order

"""
constructs with values
"""

def test_construct_with_values():
    order = Order(1, 'order_name', '2023-10-30')
    assert order.id == 1
    assert order.order_name == 'order_name'
    assert order.start_date == '2023-10-30'

"""
has string representation
"""

def test_string_representation():
    order = Order(1, 'order_name', '2023-10-30')
    assert str(order) == "Order(1, order_name, 2023-10-30)"

"""
instances with same values are equal
"""

def test_instances_with_same_values_are_equal():
    order1 = Order(1, 'order_name', '2023-10-30')
    order2 = Order(1, 'order_name', '2023-10-30')
    assert order1 == order2