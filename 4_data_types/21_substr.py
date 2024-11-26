# Program to Get a Substring of a String

string = input("Enter a string: ")
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))


def substring(string, start, end):
    return string[start:end]


# test the function
print(substring(string, start, end))
