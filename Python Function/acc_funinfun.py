# 19. Write a Python program to access a function inside a 
# function. Go to the editor
def function1(a,b):
    add = function2(a, b)
    return add
def function2(a, b):
    return a + b

print(function1(4, 2))