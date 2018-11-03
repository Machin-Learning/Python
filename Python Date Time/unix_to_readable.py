# 6. Write a Python program to convert unix timestamp string to readable date. Go to the editor
# Sample Unix timestamp string : 1284105682
# Expected Output : 2010-09-10 13:31:22
import datetime
dt=datetime.datetime.fromtimestamp(int('1284105682')).strftime('%Y-%m-%d %H:%M:%S')
print(dt)