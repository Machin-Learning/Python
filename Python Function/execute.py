# 18. Write a Python program to execute a string containing Python code.
from subprocess import call
def execute(str):
    call('python -c '+ str)

execute("print('Hello')")