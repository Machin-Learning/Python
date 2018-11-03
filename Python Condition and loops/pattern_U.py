# 28. Write a Python program to print alphabet pattern 'U'. Go to the editor
# Expected Output:

#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
for i in range(1, 8):
    if i == 7:
        print(' ' + '*'*3)
    else:
        print('*   *')