# 10. Write a Python program that accepts an integer (n) 
# and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615
n = input('Enter integer n:')
nn = n * 2
nnn = n * 3
equ = int(n) + int(nn) + int(nnn)
print(equ)