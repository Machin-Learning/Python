# 10. Write a Python program to change a given string to a 
# new string where the first and last chars have been 
# exchanged. Go to the editor
str = input('Enter a string:')
str1 = str[-1]+str[1:len(str)-1]+str[0]
print(str1)