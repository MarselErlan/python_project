class Person:
    def __init__(self, FName, LName):
        self.firstName = FName
        self.lastName = LName
    def printName(self):
        print(self.firstName, self.lastName)
x = Person("John", "Doe")
x.printName()
print("--------------------")


class Student(Person):
    pass


x1 = Student("Mike", "Olsen")
x1.printName()
print("--------------------")


# class Student(Person):
#     def __int__(self, fName, lName):
#         Person.__init__(self, fName, lName)
#

# class Student(Person):
#     def __int__(self, fName, lName):
#         super().__init__(self, fName, lName)
#         self.graduationyear = 2019
#
# x2 = Student("Mike", "Oslen")
# print(x2.graduationyear)


class Student(Person):
    def __int__(self, fName, lName, year):
        super().__init__(fName, lName)
        self.graduationyear = year


x3 = Student("Mike", "Olsen", 2019)


class Student(Person):
    def __int__(self, fName, lName, year):
        super().__init__(fName, lName)
        self.graduationyaer = year

    def welcome(self):
        print("Welcome", self.firstName, self.lastName, "to the class of", self.graduationyaer)