# Python program to convert decimal number into binary, octal and hexadecimal number system

# user input for number in decimal
dec = int(input("Enter a decimal number: "))

# conversion to binary, octal and hexadecimal number system
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
