# 2. Write a Python program to count the number of characters 
# (character frequency) in a string. Go to the editor 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
string = 'google.com'
dict={}
for i in string:
    coun = string.count(i)
    dict[i] = coun
    
print(dict)   