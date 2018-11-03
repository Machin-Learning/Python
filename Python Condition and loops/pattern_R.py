# 25. Write a Python program to print alphabet pattern 'R'. Go to the editor
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *
for i in range(1, 8):
    if i == 1 or i == 4:
        print('*' * 4)
    elif i == 2 or i == 3:
        print('*   *')
    else:
        print('*'+' '*(i-4)+'*')
