thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)

thisList1 = [100, 50, 65, 82, 23]
thisList1.sort()
print(thisList1)

thisList2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList2.sort(reverse=True)
print(thisList2)

thisList3 = [100, 50, 65, 82, 23]
thisList3.sort(reverse=True)
print(thisList3)


def myfunc(n):
    return abs(n - 50)

thisList4 = [100, 50, 65, 82, 23]
thisList4.sort(key=myfunc)
print(thisList4)


thisList5 = ["orange", "mango", "Kiwi", "Pineapple", "banana"]
thisList5.sort(key=str.lower)
print(thisList5)