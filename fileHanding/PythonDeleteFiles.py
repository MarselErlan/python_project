import os
os.remove("demoFile.txt")


if os.path.exists("demoFile.txt"):
    os.remove("demoFile.txt")
else:
    print("The file does not exist!")


os.rmdir("myFolder")