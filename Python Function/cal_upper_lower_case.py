# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output : 
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def is_up_lo(str):
    upper_case = 0
    lower_case = 0
    for i in str:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    return upper_case, lower_case

String = 'The quick Brow Fox'
upper, lower = is_up_lo(String)
print(f'No. of Upper case characters : {upper}')
print(f'No. of Lower case Characters : {lower}')