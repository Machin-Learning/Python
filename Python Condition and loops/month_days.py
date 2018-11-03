# 33. Write a Python program to convert month name to a number
#  of days. Go to the editor
# Expected Output:

# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December                                
# Input the name of Month: February                                       
# No. of days: 28/29 days 
dict_month_day={'January':31, 'February':'28/29', 'March':31,'April':30, 'May':31, 'June':30, 'July':31, 'August':31
 , 'September': 30, 'October': 31, 'November': 30, 'December': 31}
print(f'List of months:{dict_month_day.keys()}')
month = input('Input the name of Month:')
 
print(f'No. of days:{dict_month_day[month]}')