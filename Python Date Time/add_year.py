# 16. Write a Python program to add year(s) with a given date and display the new date. Go to the editor

# Sample Data : (addYears is the user defined function name) 
# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29),1))

# Expected Output : 
# 2014-01-01
# 2015-01-01
# 2017-01-01
# 2001-03-01
import datetime
def addYears(date, n):
    delta = datetime.timedelta(days=365)
    if n < 0:
        return date - (delta * abs(n))
    elif n == 0:
        return date
    elif n > 0 :
        return date + (delta * abs(n))  


print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))
