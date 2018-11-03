# 29. Write a Python program to print alphabet pattern 'X'. Go to the editor
# Expected Output:

#  *   *                                                                  
#  *   *                                                                  
#   * *                                                                   
#    *                                                                    
#   * *                                                                   
#  *   *                                                                  
#  *   *
for i in range(1, 8):
    if i <= 2 or i >= 6:
        print('*   *')
    elif i == 3 or i == 5:
        print(' * *')
    elif i == 4:
        print('  *')
    