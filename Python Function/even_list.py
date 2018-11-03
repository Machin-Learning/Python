# 10. Write a Python program to print the even numbers from a given list. Go to the editor
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8]
def print_even(list):
    lst = []
    for i in list:
        if i % 2 == 0:
            lst.append(i)
    return lst

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = print_even(List)
print(even_list)
