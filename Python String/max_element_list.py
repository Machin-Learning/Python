# 8. Write a Python function that takes a list of words and 
# returns the length of the longest one. Go to the editor 
def fun(list):
    list1=[]
    for i in list:
        list1.append(len(i))
    return max(list1)

list = ['apple', 'mango', 'orange', 'raspberry']
print(fun(list))