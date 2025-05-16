x = "Hello World!"
print(len(x))
print("---------------------")

myTuple = ("apple", "banana", "cherry")
print(len(myTuple))
print("---------------------")

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(len(thisDict))
print("---------------------")


# class Car1:
#     def __int__(self, brand1, model1):
#         self.brand1= brand1
#         self.model1 = model1
#
#     def move1(self):
#         print("Drive!")
#
# class Boat2:
#     def __init__(self, brand2, model2):
#         self.brand2 = brand2
#         self.model2 = model2
#     def move2(self):
#         print("Sail!")
#
# class Plane3:
#     def __init__(self, brand3, model3):
#         self.brand3 = brand3
#         self.model3 = model3
#     def move3(self):
#         print("Fly!")
#
# car1 = Car1("Ford", "Mustang")
# boat2 = Boat2("Idiza", "Touring 20")
# plane3 = Plane3("Boeing", "747")
#
# for i in (car1, boat2, plane3):
#     i.move1()
print("---------------------")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for i in(car1, boat1, plane1):
    print(i.brand)
    print(i.model)
    i.move()
print("---------------------")






