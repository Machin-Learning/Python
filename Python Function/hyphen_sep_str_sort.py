# 15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow
def sort(str):
    new_str = str.split('-')
    sorted_list = sorted(new_str)
    sorted_str = '-'.join(sorted_list)
    
               
    return sorted_str

string = 'green-red-yellow-black-white'
print(sort(string))
# list = [1, 2, 3, 4]
# str = str(list)
# print('-'.join(str))