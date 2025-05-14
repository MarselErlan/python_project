myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myFamily)
print("---------------------")


child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
        "name": "Tobias",
        "year": 2007
}
child3 = {
        "name": "Linus",
        "year": 2011
    }

myFamily2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myFamily2)
print("------------------")
print(myFamily2["child2"]["name"])
print("------------------")

for i, obj in myFamily2.items():
    print(i)
    for k in obj:
        print(k + ":", obj[k])


