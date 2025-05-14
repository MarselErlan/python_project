thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

thisList1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList1[1:3] = ["blackcurrant", "watermelon"]
print(thisList1)

thisList2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList2[1:2] = ["blackcurrant", "watermelon"]
print(thisList2)

thisList3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList3[1:3] = ["watermelon"]
print(thisList3)

thisList4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList4.insert(2, "watermelon")
print(thisList4)

