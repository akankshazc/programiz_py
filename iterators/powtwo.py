"""Iterator that will give us the next power of 2 in each iteration. 
Power exponent starts from zero up to a user set number"""


class PowTwo:
    """Class to implement an iterator of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(5)

# create an iterable from the object
i = iter(numbers)

# using next to get to the next iterator element
print(next(i))  # prints 1
print(next(i))  # prints 2
print(next(i))  # prints 4
print(next(i))  # prints 8
print(next(i))  # prints 16
print(next(i))  # prints 32
print(next(i))  # raises StopIteration exception
