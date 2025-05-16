myTuple = ("apple", "banana", "cherry")
myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))
print("----------------------------")

myStr1 = "Banana"
myIt1 = iter(myStr1)

print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print(next(myIt1))
print("----------------------------")

myTuple2 = ("apple", "banana", "cherry")
for i in myTuple2:
    print(i)
print("----------------------------")

myStr2 = "banana"
for i in myStr2:
    print(i)
print("----------------------------")



class myNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass3 = myNumbers()
myIter3 = iter(myclass3)

print(next(myIter3))
print(next(myIter3))
print(next(myIter3))
print(next(myIter3))
print(next(myIter3))
print("----------------------------")


class myNumbers4:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x4 = self.a
            self.a += 1
            return x4
        else:
            raise StopIteration

myclass4 = myNumbers4()
myIter4 = iter(myclass4)

for i in myIter4:
    print(i)
print("----------------------------")


