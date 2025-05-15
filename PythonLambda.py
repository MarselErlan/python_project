x = lambda a: a + 10
print(x(5))
print("-------------------------")


x1 = lambda a, b: a * b
print(x1(5, 6))
print("-------------------------")


x2 = lambda a, b, c: a + b + c
print(x2(5, 6, 2))
print("-------------------------")


def myFunc(n):
    return lambda a: a * n

myDoubler = myFunc(2)
print(myDoubler(11))
print("-------------------------")

def myFunc1(n):
    return lambda a: a * n
myTripler = myFunc1(3)
print(myTripler(11))
print("-------------------------")


def myFunc2(n):
    return lambda a: a * n

myDoubler2 = myFunc2(2)
myTripler2 = myFunc2(3)

print(myDoubler2(11))
print(myTripler2(11))
print("-------------------------")
