# 17. Write a Python program to print alphabet pattern 'A'. Go to the editor
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                  
#  *   *                                                                  
#  *   *                                                                  
#  *   *
for i in range(1, 8):
    if i == 1:
        print(' ' + '*' * 3)
    elif i == 4:
        print('*' * 5)
    else:
        print('*   *')