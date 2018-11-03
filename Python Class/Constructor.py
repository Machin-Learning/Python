class Student:
    # def __init__(self):
    #     print('con')
    # # Method/Costructor Over Loading is not in python
    def __init__(self, name):
        self.name = name
        print('constructor runing...')

s = Student('Shaikh')
s1 = Student('Khan')
print(s)

