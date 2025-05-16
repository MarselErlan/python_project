import math

print("Enter your name: ")
name = input()
print(f"Hello {name}")
print("----------------------")

name1 = input("Enter your name: ")
print(f"Hello {name1}")
print("----------------------")


name2 = input("Enter your name: ")
print(f"Hello {name2}")
fav1 = input("What is your favorite animal: ")
fav2 = input("What is your favorite color: ")
fav3 = input("What is your favorite number: ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
print("----------------------")

x3 = input("Enter a number")
y3 = math.sqrt(float(x3))
print(f"The square root of {x3} is {y3}")
print("----------------------")


y4 = True
while y4 == True:
    x4 = input("Enter a number")
    try:
        x4 = float(x4);
        y4 = False
    except:
        print("Wrong input, please try again.")
print("Thank you")

