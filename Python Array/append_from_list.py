# 9. Write a Python program to append items from a specified 
# list. Go to the editor
from array import *
list = [1, 2, 3, 4, 5]
arr = array('i', [])
for i in list:
    arr.append(i)

print(arr)