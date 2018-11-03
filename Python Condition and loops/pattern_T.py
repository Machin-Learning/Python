# 27. Write a Python program to print alphabet pattern 'T'. Go to the editor
# Expected Output:
#  *****                                                                  
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *                                                                    
#    *  
for i in range(1, 8):
    if i == 1:
        print('*' * 5)
    else:
        print('  *')