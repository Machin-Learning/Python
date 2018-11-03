# 1. Write a Python function to find the Max of three numbers. Go to the editor
def grater(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > c:
        return b
    else:
        return c

gratest = grater(1, 2, 3)
print(f'{gratest} is gratest')