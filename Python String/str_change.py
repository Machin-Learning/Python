# 4. Write a Python program to get a string from a given 
# string where all occurrences of its first char have 
# been changed to '$', except the first char itself. Go to the editor 
# Sample String : 'restart'
# Expected Result : 'resta$t'
string = 'restart'
str = ''
x=string.index(string[0],1,len(string))
for i in range(len(string)):
    if i == x:
        str += '$'
    else:
        str +=string[i]
print(str)
print(type(string.index(string[0],1,len(string))))