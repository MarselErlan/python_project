def my_function():
    print("Hello form a function")

my_function()
print("------------------")

def my_function1(fname):
    print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")
my_function1("Linus")
print("------------------")


def my_function2(fName, lName):
    print(fName + " " + lName)
my_function2("Emil", "Refsnes")
print("------------------")

def my_function3(*kids):
    print("The youngest child is " + kids[2])
my_function3("Emil", "Tobias", "Linus")
print("------------------")


def my_function4(child3, child2, child1):
    print("The youngest child is " + child3)
my_function4(child1="Emil", child2="Tobias", child3="Linus")
print("------------------")

def my_function5(**kid):
    print("His last name is " + kid["lname"])
my_function5(fname="Tobias", lname="Refsnes")
print("------------------")

def my_function6(country="Norway"):
    print("I am from " + country)
my_function6("Sweden")
my_function6("India")
my_function6()
my_function6("Brazil")
print("------------------")

def my_function7(food):
    for i in food:
        print(i)

fruits = ["apple", "banana", "cherry"]
my_function7(fruits)
print("------------------")


def my_function8(x):
    return 5 * x

print(my_function8(3))
print(my_function8(5))
print(my_function8(9))
print("------------------")


def my_function9():
    pass
print("------------------")


def my_function10(y, /):
    print(y)
my_function10(3)
print("------------------")


def my_function11(a):
    print(a)
my_function11(a=3)
print("------------------")


def my_function12(*, b):
    print(b)
my_function12(b=3)
print("------------------")


def my_function13(a, b, /, *, c, d):
    print(a + b + c + d)
my_function13(5, 6, c=7, d=8)
print("------------------")


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results: ")
tri_recursion(6)


