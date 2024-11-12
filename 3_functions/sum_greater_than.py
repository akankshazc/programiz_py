# for a given list, return the sum of numbers greater than n

def sum_greater_than(numbers, n):
    sum = 0
    for num in numbers:
        if num > n:
            sum = sum + num
    return sum
