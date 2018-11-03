# 20. Write a Python program to print alphabet pattern 'G'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *                                                                      
#  * ***                                                                  
#  *   *                                                                  
#  *   *                                                                  
#   *** 
for i in range(1, 8):
    if i == 1 or i == 7:
        print(' ' + '*' * 3)
    elif i == 4:
        print('*' + ' ' + '*' * 3)
    elif i == 3:
        print('*')
    else:
        print('*   *')    