# 3. Write a Python program to guess a number between 1 to 9.
#  Go to the editor
# Note : User is prompted to enter a guess. 
# If the user guesses wrong then the prompt appears again 
# until the guess is correct, on successful guess, user will 
# get a "Well guessed!" message, and the program will exit.
import random
random_num=random.randrange(1,10,1,int)
while True:
    user_guess = int(input('Guess a Number between 1 to 9:'))
    if user_guess == random_num:
        print('Well guessed!')
        break



