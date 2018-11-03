# 16. Write a Python function to create and print a list where the
#  values are square of numbers between 1 and 30 (both included).
def square_list():
    list = []
    for i in range(1, 31):
        list.append(i ** 2)
    return list
print(square_list())