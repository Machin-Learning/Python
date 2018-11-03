# 10. Write a Python program to insert a new item before the 
# second element in an existing array. Go to the editor
from array import *
arr = array('i',[1, 2, 3, 4, 5])
arr.insert(1, 5)
print(arr)