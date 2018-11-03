# 10. Write a Python program to add 5 seconds with the current time. Go to the editor
# Sample Data :
# 13:28:32.953088 
# 13:28:37.953088
import datetime
dt = datetime.datetime.today()
d_time = datetime.timedelta(seconds=5)
added_5sec = dt + d_time

print(f'Current Time : {dt.time()}')
print(f'Added 5 seconds Time : {added_5sec.time()}')