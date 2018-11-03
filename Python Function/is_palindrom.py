# 12. Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def is_palindrome(str):
    if str == str[::-1]:
        return True

is_palindrome = is_palindrome('madam')
print(f'The given string is palindrome:{is_palindrome}')