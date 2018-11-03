# 5. Write a Python program to subtract five days from 
# current date. Go to the editor
# Sample Date : 
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17
import datetime
cur_date=datetime.date.today()
ddalta = datetime.timedelta(days=5)
print(f'Current Date : {cur_date}')
print(f'5 days before Current Date : {cur_date-ddalta}')
