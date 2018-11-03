# 5. Write a Python program to get a single string from two 
# given strings, separated by a space and swap the first two 
# characters of each string. Go to the editor 
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'
def str_swap(s, s1):
    str1 = s[0:2]
    str2 = s1[0:2]
    for i in s[2:]:
        str2 += i
    for i in s1[2:]:
        str1 += i
    
    print(str2,str1)
            
    
str_swap('abc','xyz')