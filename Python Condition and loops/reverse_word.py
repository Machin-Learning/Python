# 5. Write a Python program that accepts a word from the user 
# and reverse it. Go to the editor
user_word = input('Enter aword:')
rev_word = ''
x = len(user_word)
for i in range(x-1,-1,-1):
    rev_word+=user_word[i]

print(rev_word)