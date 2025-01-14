import time

time_tuple = (2025, 1, 14, 23, 44, 4, 4, 362, 0)

# convert time_tuple to seconds since epoch
seconds = time.mktime(time_tuple)

print(seconds)
