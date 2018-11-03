# 22. Write a Python program to print alphabet pattern 'M'. Go to the editor
# Expected Output:

#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *
for i in range(1, 8):
    if i == 3:
        print('*' * 2 + ' ' + '*' * 2)
    elif i == 4:
        print('*' + ' ' + '*' + ' ' + '*')
    else:
        print('*   *')