# 13. Write a Python program to get week number. Go to the editor
# Sample Date : 2015, 6, 16
# Expected Output : 25
import calendar , datetime
date = datetime.datetime(2015, 6, 16)
print(date.isocalendar()[1])