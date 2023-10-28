import os

filesOnESP = os.listdir()
print("these file are on your ESP32")
for f in filesOnESP:
    print(" -> {0}".format(f))

print("the boot.py should be on every ESP!")

fileHandle = open('boot.py')
fileContent = fileHandle.read()
fileHandle.close()

print("the first line ...")
print(fileContent.split("\n", 1)[0])

print("the first 20 bytes of the file ...")
print(fileContent[0:20])

print("==========")
print("a new file is created --> newfile.txt")
print(" ... check out its content")
print(" ... when you execute the program again it will delete the file newfile.txt")

if "newfile.txt" in os.listdir():
    os.remove("newfile.txt")
else:
    newFile = open("newfile.txt", "w")
    newFile.write("something interesting is here\nexecute the program again and this file will be deleted")
    newFile.close()
