"""Create a Person class. Implement the functionality to count the number of objects created.
How would you go about this?"""

class Person():
    count = 0
    def __init__(self,name:"str",age:"int")->"None":
        """dunder method to create the instance variables"""
        Person.count += 1
        self.name = name
        self.age = age

print("no of objects created at the begining %s "%(Person.count))
person1 = Person("bala",28)
person2 = Person("smi",28)
print("no of objects created later %s "%(Person.count))