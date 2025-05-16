import myModule

myModule.greeting("Jonathan")
print("------------------")

import myModule

a = myModule.person1["age"]
print(a)
print("------------------")

import myModule as mx

a1 = mx.person1["age"]
print(a1)
print("------------------")


import platform

x = platform.system()
print(x)
print("------------------")


import platform

x1 = dir(platform)
print(x1)
print("------------------")

from myModule import person1

print(person1["age"])
