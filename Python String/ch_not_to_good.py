# 7. Write a Python program to find the first appearance of the 
# substring 'not' and 'poor' from a given string, if 'not' 
# follows the 'poor', replace the whole 'not'...'poor' 
# substring with 'good'. Return the resulting string. Go to the editor 
# Sample String : 
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
str = 'The lyrics is not that poor!'
if 'not' and 'poor' in str and str.find('not') < str.find('poor'):
    
    x = str.find('not')
    print(str[0:x] + ' good')
else:
    print(str)
