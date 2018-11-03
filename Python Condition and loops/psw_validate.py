# 15. Write a Python program to check the validity of password
#  input by users. Go to the editor
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
import re
psw = input('Enter Password:')
x = True
while x:
    if (len(psw) < 6 or len(psw) >12):
        break
    elif not re.search('[a-z]', psw):
        break
    elif not re.search('[0-9]', psw):
        break
    elif not re.search('[A-Z]',psw) :
        break
    else:
        print('Valid Password')
        x = False
        break
if x:
    print('Invalid password')