# Using __class__.__name__

class Vehicle:
    def name(self, name):
        return name


v = Vehicle()
print(v.__class__.__name__)


# Using type() and __name__ attribute

print(type(v).__name__)
