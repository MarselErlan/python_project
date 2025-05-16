def myFunc():
    x = 300
    print(x)
myFunc()
print("--------------------------------")

def myFunc():
    x = 300
    def myInnerFunc():
        print(x)
    myInnerFunc()
myFunc()
print("--------------------------------")


x = 300
def myFunc():
    print(x)
myFunc()
print(x)
print("--------------------------------")


x = 300
def myFunc():
    x = 200
    print(x)
myFunc()
print(x)
print("--------------------------------")


def myFunc():
    global x
    x = 300
myFunc()
print(x)
print("--------------------------------")


x = 300
def myFunc():
    global x
    x = 200
myFunc()
print(x)
print("--------------------------------")


def myFunc1():
    x = "Jane"
    def myFunc2():
        nonlocal x 
        x = "hello"
    myFunc2()
    return x
print(myFunc1())