import os

filename = "csvtest.txt"
delimiter = ","

if filename in os.listdir():
    print("found {}".format(filename))
    f = open(filename, "r")
    
    for line in f:
        v = line.strip().split(delimiter)
        print("\nvalue of second column: {}".format(v[1]))
        
        if (int(v[2]) > 10):
            print("value of third column is > 10")
        else:
            print("value of third column is NOT > 10")

    f.close()

    os.remove(filename)
else:
    newFile = open(filename, "w")
    newFile.write("1,2,3\n4,5,6\n7,8,9\n10,11,12\n13,14,15\n16,17,18")
    newFile.close()
    print("created file {}\nplease restart the program".format(filename))
