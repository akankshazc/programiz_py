# Program to create a nested directory

# using pathlib

# importing the pathlib module
import os
from pathlib import Path

# creating a directory
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)

# using os module

# importing os module

# creating a directory
try:
    os.makedirs("/root/dirA/dirB")
except FileExistsError:
    print("Directory already exists")
