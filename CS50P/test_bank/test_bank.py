from bank import value

def test_value_starts_with_h():
    assert value("Hi") == 20

def test_value_is_hello():
    assert value("Hello") == 0

def test_value_not_h():
    assert value("bob") == 100

