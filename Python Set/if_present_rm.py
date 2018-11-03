# 5. Write a Python program to remove an item from a set 
# if it is present in the set. Go to the editor
set = {1, 2, 3, 4, 5, 6}
n = 7
if n in set:
    set.remove(n)
else:
    print(f'{n} is not in set')

print(set)