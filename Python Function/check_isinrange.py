# 6.Write a Python function to check whether a number is in a 
# given range. Go to the editor
def check(a, n):
    if a in n:
        return True
    else:
        return False
result = check(4, list(range(1,5)))
print(result)
