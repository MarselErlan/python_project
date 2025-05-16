f = open("domeFile.txt")
print(f.read)


f1 = open("D:\\myFiles\welcome.txt")
print(f.read())


with open("demoFile.txt") as f2:
    print(f2.read())


f3 = open("demoFile.txt")
print(f3.readline())
f3.close()


with open("demoFile.txt") as f4:
    print(f4.read(5))

with open("demoFile.txt") as f5:
    print(f5.readline())

with open("demoFile.txt") as f6:
    print(f6.readline())
    print(f6.readline())


with open("demoFile.txt") as f7:
    for i in f7:
        print(i)

