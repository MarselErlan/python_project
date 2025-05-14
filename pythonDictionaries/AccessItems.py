thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisDict["model"]
y = thisDict.get("model")
z = thisDict.keys()
e = thisDict.values()
d = thisDict.items()
print(x)
print(y)
print(z)
print(e)
print(d)

print("------------------")

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

w = car.keys()
print(w)
car["color"] = "white"
print(w)
print("------------------")


car1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

c = car1.values()
print(c)
car1["year"] = 2020
print(c)
print("------------------")


car2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

r = car2.items()
print(r)
car2["year"] = 2020
print(r)
print("------------------")


thisDict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisDict1:
    print("Yes, 'model' is one of the keys in the thisDict dictionary")
