# 8. Write a Python program to convert an array to an 
# array of machine values and return the bytes representation. Go to the editor 
from array import *
arr = array('i', [1, 2, 3, 4, 5])
print(arr.tobytes())