# 2. Write a Python function to sum all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 
def list_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum
List = [8, 2, 3, 0, 7]
add = list_sum(List)
print(add)
