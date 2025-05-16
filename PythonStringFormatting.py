txt = f"The price is 49 dollars"
print(txt)
print("------------------------")


price = 59
txt = f"The price is {price} dollars"
print(txt)
print("------------------------")


price2 = 59
txt2 = f"The price is {price2:.2f} dollars"
print(txt2)
print("------------------------")


txt3 = f"The price is {95:.2f} dollars"
print(txt3)
print("------------------------")


txt4 = f"The price is {20 * 59} dollars"
print(txt4)
print("------------------------")

price5 = 59
tax = 0.25
txt5 = f"The price is {price5 + (price5 + tax)} dollars"
print(txt5)
print("------------------------")


price6 = 49
txt6 = f"It is very {'Expensive' if price6>50 else 'Cheap'}"
print(txt6)
print("------------------------")


fruit7 = "apple"
txt7 = f"I love {fruit7.upper()}"
print(txt7)
print("------------------------")


def myConverter(x):
    return x * 0.3048

txt8 = f"The plane is flying at a {myConverter(30000)} meter altitude"
print(txt8)
print("------------------------")

price9 = 59000
txt9 = f"The price is {price:,} dollars"
print(txt9)
print("------------------------")



price10 = 49
txt10 = "The price is {} dollars"
print(txt10.format(price10))
print("------------------------")


txt11 = "The price is {:.2f} dollars"
print("------------------------")


quantity11 = 3
itemno11 = 567
price11 = 49
myOrder11 = "I want {} pieces of item number {} for {:.2f} dollars."

print(myOrder11.format(quantity11, itemno11, price11))
print("------------------------")



