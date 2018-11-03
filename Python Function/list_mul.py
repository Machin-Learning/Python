# 3. Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336 
def list_mul(list):
    mul = 1
    for i in list:
        mul *= i
    return mul

List = [8, 2, 3, -1, 7]
multi = list_mul(List)
print(multi)
