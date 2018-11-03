class Student:
    '''This is class for Student'''
    cname = 'VIT'
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def info(self):
        x = 20
        print('$' * 20)
        print(f'My Name is {self.name}')
        print(f'My Rollno is {self.rollno}')
        print('$' * 20)
    @classmethod
    def getcname(cls):
        print(f'College name is {cls.cname}')
    @staticmethod
    def static(a, b):
        print(a, b)
    
s1 = Student('Muzmmil', 100)
s2 = Student('Sabnam', 200)
s1.info()
Student.getcname()
s2.info()
s2.getcname()
Student.static(4, 5)
