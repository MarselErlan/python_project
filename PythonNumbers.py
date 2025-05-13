"""
int
float
complex
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex

print(type(x))
print(type(y))
print(type(z))


# int

x1 = 1
y1 = 123456789098765432345678
z1 = -765434567

print(type(x1))
print(type(y1))
print(type(z1))

# float

x2 = 1.10
y2 = 1.0
z2 = -35.59

x3 = 35e3
y3 = 12E4
z3 = -35.5e100

print(type(x2))
print(type(y2))
print(type(z2))
print(type(x3))
print(type(y3))
print(type(z3))

# complex

x4 = 3 + 5j
y4 = 5j
z4 = -5j

print(type(x4))
print(type(y4))
print(type(z4))


x5 = 1  # int
y5 = 2.8  # float
z5 = 1j  # complex

# convert from int to float:
a = float(x5)
# convert from float to int:
b = int(y5)
# convert from int to complex
c = complex(x5)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


import random
print(random.randrange(1, 10))


