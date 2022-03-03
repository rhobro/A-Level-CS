#!/bin/python3


# the Class is a template for creating a person
class Person():
    def __init__(self, fname, lname):
        self.setname(fname, lname)
        print("Created a new person called", self.getname())
    
    def setname(self, fname, lname): # public
        self.firstname = fname
        self.lastname = lname

    def getname(self): # public
        return self.firstname + " " + self.lastname

    def set_username(self, uname):
        self.uname = uname

    def set_password(self, password):
        if len(password) >= 8:
            self.password = password


class Student(Person):

    def __init__(self, fname, lname, form):
        super().__init__(fname, lname)
        self.form = form

class Teacher(Person):
    
    def __init__(self, fname, lname, title):
        self.title = title
        super().__init__(fname, lname)
    
    def getname(self):
        return self.title + " " + self.firstname + " " + self.lastname

    

# Instantiation  -  creating an Instance of a person
p1 = Teacher("Lucy", "Smith", "Mrs")


print(p1.firstname)    # this works in Python, but in other lanwguages we should
                       # set the attributes to Private

print( p1.getname() )  # we should use the getter to retrieve the name, rather than
                       # accessing the name directly. This is called encapsulation.
                       
p1.setname("Lucy","Jones")
print( p1.getname() )

p2 = Person("Bob", "Ross")