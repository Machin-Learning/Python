# 4. Write a Python script to check if a given key already 
# exists in a dictionary. Go to the editor
def check_key(dict, key):
    if key in dict.keys():
        return True
    else:
        return False
dict = {1: 'one', 2: 'two', 3: 'three'}
print(check_key(dict,4))