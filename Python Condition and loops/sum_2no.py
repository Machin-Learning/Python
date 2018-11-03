# 34. Write a Python program to sum of two given integers. 
# However, if the sum is between 15 to 20 it will return 20. Go to the editor
x = int(input('Enter 1st no.:'))
y = int(input('Enter 2nd no.:'))
z = x + y
if z>=15 and z<=20:
    print('20')