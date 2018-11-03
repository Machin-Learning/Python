# 5. Write a Python program to get the current memory address 
# and the length in elements of the buffer used to hold an 
# array?s contents and also find the size of the memory 
# buffer in bytes. Go to the editor 
from array import *
arr = array('i', [1, 2, 3, 4, 5])
print(arr.buffer_info())