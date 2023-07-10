import pytest
from jar import Jar

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7

def test_capacity_exceeded():
    jar = Jar(capacity=10)
    with pytest.raises(ValueError):
        jar.deposit(12)

def test_not_enough_cookies():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(5)

def test_str_representation():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_capacity_property():
    jar = Jar(capacity=10)
    assert jar.capacity == 10

def test_size_property():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(capacity=-5)
