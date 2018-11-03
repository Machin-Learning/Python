# 12. Write a Python program that accepts a sequence of lines 
# (blank line to terminate) as input and prints the lines as 
# output (all characters in lower case). Go to the editor
line = input('Enter a blank line\n')
list = []
for i in range(len(line)):
    list.append(line)
for j in list:
    print(j)