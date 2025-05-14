thisList = ["apple", "banana", "cherry"]

for i in thisList:
    print(i)

thisList1 = ["apple", "banana", "cherry"]

for i in range(len(thisList1)):
    print(thisList1[i])


thisList2 = ["apple", "banana", "cherry"]

i = 0
while i < len(thisList2):
    print(thisList2[i])
    i = i + 1


thisList3 = ["apple", "banana", "cherry"]
[print(x) for x in thisList3]