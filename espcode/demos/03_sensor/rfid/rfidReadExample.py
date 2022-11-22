import mfrc522
from os import uname

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

def do_read():
    rdr = mfrc522.MFRC522(sck=18, mosi=23, miso=19, rst=22, cs=21)

    print("")
    print("Place card before reader to read from address 0x08")
    print("")

    try:
        while True:
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, uid) = rdr.SelectTagSN()
                if stat == rdr.OK:
                    print("Card detected %s" % uidToString(uid))
                else:
                    print("Authentication error")
    except KeyboardInterrupt:
        print("Bye")

do_read()