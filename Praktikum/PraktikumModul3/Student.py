from Person import Person

class Student(Person):
    def __init__(self,fname,lname):
        super(Student, self).__init__(fname,lname)