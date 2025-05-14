
"""

union()
update()
intersection()
difference()
symmetric_difference()

"""


# union()


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print("-----------------------")

set4 = {"a", "b", "c"}
set5 = {1, 2, 3}

set6 = set4 | set5
print(set6)
print("-----------------------")


set7 = {"a", "b", "c"}
set8 = {1, 2, 3}
set9 = {"John", "Elena"}
set10 = {"apple", "bananas", "cherry"}

mySet = set7.union(set8, set9, set10)
print(mySet)
print("-----------------------")


set11 = {"a", "b", "c"}
set12 = {1, 2, 3}
set13 = {"John", "Elena"}
set14 = {"apple", "bananas", "cherry"}

mySet1 = set11 |set12 | set13 | set14
print(mySet1)
print("-----------------------")


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)
print("-----------------------")



# update()



set15 = {"a", "b", "c"}
set16 = {1, 2, 3}
set15.update(set16)
print(set15)
print("-----------------------")



# intersection()



set17 = {"apple", "banana", "cherry"}
set18 = {"google", "microsoft", "apple"}

set19 = set17 & set18
print(set19)
print("-----------------------")

set20 = {"apple", "banana", "cherry"}
set21 = {"google", "microsoft", "apple"}

set20.intersection_update(set21)
print(set20)
print("-----------------------")

set22 = {"apple", 1, "banana", 0, "cherry"}
set23 = {False, "google", 1, "apple", 2, True}

set24 = set22.intersection(set23)
print(set24)
print("-----------------------")


# difference()


set25 = {"apple", "banana", "cherry"}
set26 = {"google", "microsoft", "apple"}

set27 = set25.difference(set26)
print(set27)
print("-----------------------")


set28 = {"apple", "banana", "cherry"}
set29 = {"google", "microsoft", "apple"}

set30 = set28 - set29
print(set30)
print("-----------------------")


set31 = {"apple", "banana", "cherry"}
set32 = {"google", "microsoft", "apple"}

set31.difference_update(set32)
print(set31)
print("-----------------------")




# symmetric_difference()



set33 = {"apple", "banana", "cherry"}
set34 = {"google", "microsoft", "apple"}

set35 = set33.symmetric_difference(set34)
print(set35)
print("-----------------------")


set36 = {"apple", "banana", "cherry"}
set37 = {"google", "microsoft", "apple"}

set38 = set36 ^ set37
print(set38)
print("-----------------------")


set39 = {"apple", "banana", "cherry"}
set40 = {"google", "microsoft", "apple"}

set39.symmetric_difference_update(set40)
print(set39)
print("-----------------------")