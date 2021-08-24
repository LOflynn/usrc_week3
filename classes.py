class Person():
    def __init__(self, first_name):
        self.name = first_name
    
    def print_name(self):
        print("My name is", self.name)

class Student(Person):
    def __init__(self, first_name, school):
        Person.__init__(self, first_name)
        self.school = school

    def print_school(self):
        print("My school is ", self.school)
    

x = Person("Harry")
y = Student("Mark", "SchoolA")

x.print_name()

y.print_name()
y.print_school()