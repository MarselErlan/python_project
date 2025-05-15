class MyClass:
    x = 5
print("------------")

p1 = MyClass()
print(p1.x)
print("------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)
print("------------")


# class Person3:
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
# p3 = Person3("John", 36)
# print(p3.name)
# print(p3.age)


class Person4:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p4 = Person4("John", 36)
print(p4)
print("----------------------")

class Person5:
    def __int__(self, name, age):
        self.name = name
        self.age = age
    def myFunc5(self):
        print("Hello my name is " + self.name)
p5 = Person5("John", 36)
p5.myFunc5()
print("----------------------")


class Person6:
    def __int__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myFunc6(abc):
        print("Hello my name is " + abc.name)

p6 = Person6("John", 36)
p6.myFunc6()

p6.age = 40
del p6.age
del p6

class Person:
    pass

