import time

# seconds passed since epoch
seconds = 1736876626.3337157

# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)

print("Local time:", local_time)
