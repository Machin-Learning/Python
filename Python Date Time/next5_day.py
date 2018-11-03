# 9. Write a Python program to print next 5 days starting 
# from today. Go to the editor
import datetime
today = datetime.date.today()
delta = datetime.timedelta(days=5)
after_5days = today + delta
i = 1
while i <= 5:
    print(today + datetime.timedelta(days=i))
    i += 1
