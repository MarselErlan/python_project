fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(red)
print(green)
print(yellow)
print("--------------------------")

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits1

print(green)
print(yellow)
print(red)
print("--------------------------")

fruits2 = ("apple", "mango", "cherry", "papaya", "pineapple", "raspberry")
(green, *tropic, red) = fruits2

print(green)
print(tropic)
print(red)



