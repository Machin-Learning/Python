# 8. Write a Python script to merge two Python dictionaries. Go to the editor
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
# d.update(d2)
# print(d)
# or
for key, value in d2.items():
    d[key] = value
print(d)
print(d1)