fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for i in fruits:
    if "a" in i:
        newList.append(i)
print(newList)


fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newList1 = [i for i in fruits1 if "a" in i]
print(newList1)

newList2 = [i for i in fruits1 if i != "apple"]
print(newList2)

newList3 = [i for i in fruits1]
print(newList3)

newList4 = [i for i in range(10)]
print(newList4)

newList5 = [i for i in range(10) if i < 5]
print(newList5)

newList6 = [i.upper() for i in fruits1]
print(newList6)

newList7 = ['hello' for i in fruits1]
print(newList7)

newList8 = [i if i != "banana" else "orange" for i in fruits1]
print(newList8)