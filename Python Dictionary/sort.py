# 1. Write a Python script to sort
#  (ascending and descending) a dictionary by value. Go to the editor
dict = {'one': 1,
        'Four': 4,
        'Two': 2,
        'Three': 3,
        'Five': 5,
        }

x = sorted(dict.values())
y = x[::-1]
print(sorted(dict.items()))
print(x,y)