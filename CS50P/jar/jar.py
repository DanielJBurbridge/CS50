class Jar:
    def __init__(self, capacity=12):

        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Capacity exceeded")

        self.size += n

    def withdraw(self, n):
        if self.size- n < 0:
            raise ValueError("Not enough cookies")

        self.size -= n

    def capacity(self):
        return self.capacity

    def size(self):
        return self.size