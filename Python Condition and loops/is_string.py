# 35. Write a Python program to check a string represent an 
# integer or not. Go to the editor
# Expected Output:

# Input a string: Python                                                  
# The string is not an integer.  
string = input('Input a string:')
if string.isdecimal():
    print('The string is a integer')
else:
    print('The string is not an integer')
