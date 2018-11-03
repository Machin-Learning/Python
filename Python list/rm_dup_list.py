# 7. Write a Python program to remove duplicates from a list. Go to the editor
list = [1, 1, 2, 1, 3, 4, 5, 1, 2]
print(list)
set = set(list)
list1 = []
for i in set:
    list1.append(i)
print(list1)