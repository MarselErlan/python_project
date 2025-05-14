x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y)
print(thisTuple)

thisTuple1 = ("apple", "banana", "cherry")
y = ("orange",)
thisTuple1 += y
print(thisTuple1)

thisTuple2 = ("apple", "banana", "cherry")
y = list(thisTuple2)
y.remove("apple")
thisTuple2 = tuple(y)
print(thisTuple2)

thisTuple3 = ("apple", "banana", "cherry")
del thisTuple3
# print(thisTuple3)