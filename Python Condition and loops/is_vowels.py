# 32. Write a Python program to check whether an alphabet is 
# a vowel or consonant. Go to the editor
# Expected Output:

# Input a letter of the alphabet: k                                       
# k is a consonant.
char = input('Input a letter of the alphabet:')
if char in 'aeiouAEIOU':
    print(f'{char} is a Vowel')
else:
    print(f'{char} is consonant')
