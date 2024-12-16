# Program to catch multiple exceptions in one line

string = input("Enter a string: ")

try:
    num = int(input("Enter a number: "))
    print(string + num)
except (ValueError, TypeError) as e:
    print("An error occurred")
    print(e)
