# 9. Write a Python program to find the repeated items of 
# a tuple. Go to the editor
tuple = 1, 2, 3, 4, 1, 2, 4, 5
list = []
for i in tuple:
    if i not in list:
        list.append(i)
    else:
        print(i)