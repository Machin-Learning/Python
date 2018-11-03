# 11. Write a Python program to convert Year/Month/Day to 
# Day of Year in Python. Go to the editor
import datetime
dt = datetime.datetime.today()
date = dt.date()
print(date.day)
