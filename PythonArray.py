cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

x = cars[0] = "Toyota"
print(x)

c = len(cars)
print(c)

for i in cars:
    print(i)

cars.append("Honda")
cars.pop(1)
cars.remove("Volvo")

"""
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
"""