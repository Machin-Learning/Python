# 6. Write a Python program to add 'ing' at the end of a given
#  string (length should be at least 3). If the given string 
# already ends with 'ing' then add 'ly' instead. If the 
# string length of the given string is less than 3, 
# leave it unchanged. Go to the editor 
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'
str = input('Enter a String:')
str1=''
if len(str) < 3:
    print(str)
elif str.endswith('ing'):
    print(str+'ly')
else:
    for i in str:
        str1 += i
    
    print(str1+'ing')

# str = 'Hello'
# print(str.endswith('llo'))