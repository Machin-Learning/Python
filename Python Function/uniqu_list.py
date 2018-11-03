# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. Go to the editor
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(list):
    lst = []
    for i in list:
        if i not in lst:
            lst.append(i)
    return lst

List = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = unique_list(List)
print(f'Unique List : {unique_list}')
