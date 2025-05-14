thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisDict.pop("model")
print(thisDict)
thisDict.popitem()
print(thisDict)
del thisDict["brand"]
print(thisDict)
print("--------------------")

thisDict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisDict1
# print(thisDict1)
print("-------------")

thisDict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisDict2.clear()
print(thisDict2)