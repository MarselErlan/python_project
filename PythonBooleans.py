print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
# the following will return True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# the following will return False
print(bool(False))
print(bool(None))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myClass():
    def __len__(selfs):
        return 0
myobj = myClass()
print(bool(myobj))

def myFunction():
    return True
print(myFunction())
if myFunction():
    print("Yes!")
else:
    print("No!")

x1 = 200
print(isinstance(x, int))