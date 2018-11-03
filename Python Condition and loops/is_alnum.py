# 14. Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
# Sample Data : Python 3.2
# Expected Output :
# Letters 6 
# Digits 2
string = input('Input a string:')
letters = 0
Digits = 0
for let_dig in string:
    if let_dig.isalpha():
        letters += 1
    elif let_dig.isdigit():
        Digits += 1
print(f'Letter {letters}')
print(f'Digits {Digits}')

