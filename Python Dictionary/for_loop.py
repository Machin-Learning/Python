# 5. Write a Python program to iterate over dictionaries using
#  for loops. Go to the editor
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for value in dict.values():
    print(value,end=' ')
for key in dict.keys():
    print(key,end=' ')
for key,value in dict.items():
    print(key,value,end=' ')

for key, value in enumerate(dict.items()):
    print(key,value)