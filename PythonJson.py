import json

# convert from json to python

x = '{"name": "john", "age": 30, "city": "New York"}'
y = json.loads(x)
print(y["age"])
print("------------------------")

# convert from python to json

x1 = {
    "name": "john",
    "age": 30,
    "city": "New York"
}

y1 = json.dumps(x1)
print(y)
print("------------------------")

"""
You can convert Python objects of the following types, into JSON strings:

    dict
    list
    tuple
    string
    int
    float
    True
    False
    None

"""
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
print("------------------------")

"""
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
Python 	JSON

dict 	---> Object
list 	---> Array
tuple 	---> Array
str 	---> String
int 	---> Number
float 	---> Number
True 	---> true
False 	---> false
None 	---> null

"""


x2 = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x2))
print("------------------------")

print(json.dumps(x2, indent=4))
print("------------------------")

print(json.dumps(x2, indent=4, separators=(".", "=")))
print("------------------------")

print(json.dumps(x2, indent=4, sort_keys=True))



