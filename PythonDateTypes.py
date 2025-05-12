"""

text type: str
numeric types: int, float, complex
sequence types: list, tuple, range
mapping type: dict
set types: set, frozenset
boolean tupe: bool
Binary types: bytes, bytearray, memoryview
none type: NoneType

"""


x = 5
print(type(x))


# 1 -- str
x1 = "Hello World"
print(x)
print(type(x))

# 2 -- int

x2 = 20
print(x2)
print(type(x2))


# 3 -- float

x3 = 20.5
print(x3)
print(type(x3))

# 4 -- complex

x4 = 1j
print(x4)
print(type(x4))

# 5 -- list

x5 = ["apple", "banana", "cherry"]
print(x5)
print(type(x5))

# 6 -- tuple

x6 = ("apple", "banana", "cherry")
print(x6)
print(type(x6))

# 7 -- range

x7 = range(6)
print(x7)
print(type(x7))

# 8 -- dict

x8 = {"name": "John", "age": 3}
print(x8)
print(type(x8))

# 9 -- set

x9 = {"apple", "banana", "cherry"}
print(x9)
print(type(x9))

# 10 -- frozenset

x10 = frozenset({"apple", "banana", "cherry"})
print(x10)
print(type(x10))

# 11 -- bool

x11 = True
print(x11)
print(type(x11))

# 12 -- bytes

x12 = b"Hello"
print(x12)
print(type(x12))

# 13 -- bytearray

x13 = bytearray(5)
print(x13)
print(type(x13))

# 14 -- memoryview

x14 = memoryview(bytes(5))
print(x14)
print(type(x14))

# 15 -- NoneType

x15 = None
print(x15)
print(type(x15))


