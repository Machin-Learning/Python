# 10. Write a Python program to find the list of words that 
# are longer than n from a given list of words. Go to the editor
def find_lrg(list, n):
    for word in list:
        if len(word) > n:
            print(word)

find_lrg(['mam','com','sum','num','gameing'],4)
    
