# 18. Write a Python program to print alphabet pattern 'D'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  **** 
for i in range(1, 8):
    if i == 1 or i == 7:
        print('*' * 4)
    else:
        print('*   *')