# 7. Write a Python program to print yesterday, today, tomorrow. Go to the editor
import datetime
t_day = datetime.date.today()
d_date = datetime.timedelta(days=1)
yesterday = t_day - d_date
tommoro = t_day + d_date
print(f'Today : {t_day}')
print(f'Yesterday : {yesterday}')
print(f'Tommoro : {tommoro}')