# 5. Write a Python function to calculate the factorial of a 
# number (a non-negative integer). The function accepts the 
# number as an argument. Go to the editor
def fact(n):
    facto=1
    for i in range(1, n + 1):
        facto *= i
    return facto
n = int(input('Input n for factorial:'))
result = fact(n)
print(result)