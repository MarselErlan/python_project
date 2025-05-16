with open("demoFile.txt", "a") as f:
    f.write("Now the file has more content")

with open("demoFile.txt") as f1:
    print(f1.read())

with open("demoFile.txt", "w") as f2:
    f2.write("Woops! I have deleted the content!")

with open("demoFile.txt") as f3:
    print(f3.read())

f4 = open("myFile.txt", "x")

