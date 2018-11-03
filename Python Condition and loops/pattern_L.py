# 21. Write a Python program to print alphabet pattern 'L'. Go to the editor
# Expected Output:

#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****
for i in range(1, 8):
    if i == 7:
        print('*' * 5)
    else:
        print('*')