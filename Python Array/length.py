# 4. Write a Python program to get the length in bytes of one 
# array item in the internal representation. Go to the editor
from array import *
arr = array('i', [1, 2, 3, 4, 5])
print(arr.itemsize)