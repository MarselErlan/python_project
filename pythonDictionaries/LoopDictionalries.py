thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for i in thisDict:
    print(i)
print("---------------------")

for i in thisDict:
    print(thisDict[i])
print("---------------------")

for i in thisDict.values():
    print(i)
print("---------------------")

for i in thisDict.keys():
    print(i)
print("---------------------")

for i, j in thisDict.items():
    print(i, j)
