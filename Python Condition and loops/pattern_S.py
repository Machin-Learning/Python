# 26. Write a Python program to print the following patterns. Go to the editor
# Expected Output:

#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 
 
#  ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo 
for i in range(1,8):
    if i == 1 or i == 7:
        print('*' * 5)
    elif i == 2 or i == 3:
        print('*')
    elif i == 4:
        print('*' * 5)
    elif i == 5 or i == 6:
        print('    *')
for i in range(1,6):
    if i == 1 :
        for j in range(1, 4):
            print('o'*17)
    elif i == 2 :
        for k in range(1, 4):
            print('o'*4)
    elif i == 3:
        for l in range(1, 4):
            print('o'*17)
    elif i == 4:
        for m in range(1, 4):
            print(' ' * 13 + 'o' * 4)
    else:
        for n in range(1, 4):
            print('o'*17)