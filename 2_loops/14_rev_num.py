# Python program to reverse a number

num = int(input("Enter a number: "))
rev = 0

# using a while loop
while num > 0:
    rev = rev * 10 + (num % 10)
    num = num // 10


# using string slicing
rev1 = int(str(num)[::-1])

print("Reversed number:", rev)
