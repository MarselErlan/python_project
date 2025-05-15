fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
print("--------------")

for i in "banana":
    print(i)
print("--------------")

fruits1 = ["apple", "banana", "cherry"]
for i in fruits1:
    print(i)
    if i == "banana":
        break
print("--------------")

fruits2 = ["apple", "banana", "cherry"]
for i in fruits2:
    if i == "banana":
        break
    print(i)
print("--------------")

fruits3 = ["apple", "banana", "cherry"]
for i in fruits3:
    if i == "banana":
        continue
    print(i)
print("--------------")

for i in range(6):
    print(i)
print("--------------")

for i in range(2, 6):
    print(i)
print("--------------")

for i in range(2, 30, 3):
    print(i)
print("--------------")

for i in range(6):
    print(i)
else:
    print("Finally finished!")
print("--------------")

for i in range(6):
    if i == 3: break
    print(i)
else:
    print("Finally finished")
print("--------------")

adj1 = ["red", "big", "tasty"]
fruits1 = ["apple", "banana", "cherry"]

for i in adj1:
    for j in fruits1:
        print(i, j)
print("--------------")

for i in [0, 1, 2]:
    pass

