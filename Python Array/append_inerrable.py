# 7. Write a Python program to append items from inerrable to 
# the end of the array. Go to the editor 
from array import *
arr = array('i', [1, 2, 3, 4, 5])
arr.append(arr[-1])
print(arr)