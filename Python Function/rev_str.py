# 4. Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def rev_str(str):
    rev_str = ''
    for i in range(len(str) - 1, -1, -1):
        rev_str += str[i]
    return rev_str

rev_str = rev_str("1234abcd")
print(rev_str)