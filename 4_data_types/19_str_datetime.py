# Program to convert string to datetime

from datetime import datetime

date_str = '2021-08-25'
date_dt = datetime.strptime(date_str, '%Y-%m-%d')
print(date_dt)
