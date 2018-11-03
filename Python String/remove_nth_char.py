# 9. Write a Python program to remove the nth index character 
# from a nonempty string. Go to the editor
str = input('Enter a String:')
nth_index = int(input('Enter the nth index:'))
str1 = ''
for i in range(len(str)):
    if i == nth_index:
        continue
    else:
        str1 += str[i]
print(str1)