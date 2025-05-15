a = 33
b = 200
if b > a:
    print("b is greater than a")
print("--------------------")


a1 = 33
b1 = 33

if b1 > a1:
    print("b1 is greater than a1")
elif a1 == b1:
    print("a1 and b1 are equal")
print("--------------------")


a2 = 200
b2 = 33

if b2 > a2:
    print("b2 is greater than a2")
elif a2 == b2:
    print("a2 and b2 are equal")
else:
    print("a2 is greater than b2")
print("--------------------")



a3 = 200
b3 = 33

if b3 > a3:
    print("b3 is greater than a3")
else:
    print("b3 is not greater than a3")
print("--------------------")



if a3 > b3: print("a3 is greater than b3")
print("--------------------")


a4 = 2
b4 = 330

print("A4") if a4 > b4 else print("B4")
print("--------------------")


a5 = 330
b5 = 330
print("A5") if a5 > b5 else print("=") if a5 == b5 else print("b5")
print("--------------------")


a6 = 200
b6 = 33
c6 = 500

if a6 > b6 and c6 > a6:
    print("Both conditions are True")
print("--------------------")

if a6 > b6 or a6 > c6:
    print("At least one of conditions is True")
print("--------------------")

a7 = 33
b7 = 200

if not a7 > b7:
    print("a7 is NOT greater than b7")
print("--------------------")


x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
print("--------------------")


a8 = 33
b8 = 200

if b8 > a8:
    pass

