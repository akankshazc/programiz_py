# Program to create a countdown timer

import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Fire in the hole!!")


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
