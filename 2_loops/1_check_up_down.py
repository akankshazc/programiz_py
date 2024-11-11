# Python function to return 'Up' if the input number is positive,
# 'Down' if its negative and 'Zero' if its zero.

def up_down(n):
    if n > 0:
        return 'Up'
    elif n == 0:
        return 'Zero'
    else:
        return 'Down'
