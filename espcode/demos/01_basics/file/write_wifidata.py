print("This script will setup your wifi credentials.\n\n")
print(" !!! ATTENTION !!!")
print("The following files will be MODIFIED and the contents lost:")
print("   * wifi_ssid.txt")
print("   * wifi_pass.txt")
print("   * boot.py")
print("   * lib/customnetwork.py")
print(" !!! ATTENTION !!!")
print("\n")

confirm = input("Do you want to continue? Enter 'y' to continue: ")
if confirm == "y":
    print("To setup your wifi, we need the SSID and password ...")
    ssid = input("Please enter the SSID: ")
    password = input("Please enter the password: ")
    print("")
    print("The SSID you entered is: {0}".format(ssid))
    print("The password you entered is: {0}".format(password))
    print("")
    confirm = input("Is this information correct? Enter 'y' to continue: ")
    if confirm == "y":
        print("OK - writing to flash ...")
        try:
            print("   ... writing to wifi_ssid.txt")
            fileSsid = open('wifi_ssid.txt', 'w')
            fileSsid.write(ssid)
            fileSsid.close()
            print("   ... done")
        except:
            print("ERROR: writing to file wifi_ssid.txt failed")
        
        try:
            print("   ... writing to wifi_pass.txt")
            filePassword = open('wifi_pass.txt', 'w')
            filePassword.write(password)
            filePassword.close()
            print("   ... done")
        except:
            print("ERROR: writing to file wifi_pass.txt failed")
           
        try:
            print("   ... writing to lib/customnetwork.py")
            fileCn = open('lib/customnetwork.py', 'w')
            fileCn.write("""class customnetwork:
    def setupSTA():
        import network
        import time
        
        # default credentials
        wifi_ssid = "esp32-iot"
        wifi_pass = "123456"
        
        # read from first line of files if found
        try:
            fileSsid = open('wifi_ssid.txt')
            filePassword = open('wifi_pass.txt')
            ssid = fileSsid.readline().strip()
            password = filePassword.readline().strip()
            fileSsid.close()
            filePassword.close()
            wifi_ssid = ssid
            wifi_pass = password
            if password == "":
                return
        except:
            pass
        
        wlan = network.WLAN(network.STA_IF)
        if not wlan.isconnected():
            wlan.active(True)
            macAddress = wlan.config("mac") #or machine.unique_id()
            host = "esp32-" + "".join("{:02x}".format(b) for b in macAddress[3:])
            wlan.config(dhcp_hostname = host)
            wlan.connect(wifi_ssid, wifi_pass)
            #wlan.ifconfig(config=('192.168.0.101', '255.255.255.0', '192.168.1.1', '8.8.8.8')) # (ip, subnet_mask, gateway, DNS_server)
            print("trying to connect to {0} as host {1}".format(wifi_ssid, host))
            while not wlan.isconnected():
                print("trying ... [{}]".format(time.time()))
                time.sleep(1)
                #machine.idle()
        else:
            print("board already connected to {}".format(wlan.config("essid")))
            
        customnetwork.printNetworkInformation()

    def setupAP():
        import network
        import time
        
        wifi_ssid = "esp32-wifi-" + "".join("{:02x}".format(b) for b in macAddress[3:])
        wifi_pass = "123456"
        
        wlan = network.WLAN(network.AP_IF)
        wlan.active(True)
        wlan.config(essid = wifi_ssid, password = wifi_pass)
        
        while wlan.active() == False:
            print("creating ap ... [{}]".format(time.time()))
            time.sleep(1)
            
        print("ap created")
        customnetwork.printNetworkInformation()

    def printNetworkInformation(detail = False):
        import network
        wlan = network.WLAN()
        ni = wlan.ifconfig()
        print("----- network information -----")
        print("SSID: {0}".format(wlan.config("essid")))
        print("IP: {0}".format(ni[0]))
        if detail == True:
            print("Subnetmask: {0}".format(ni[1]))
            print("Gateway: {0}".format(ni[2]))
            print("DNS: {0}".format(ni[3]))
        print("-------------------------------")

    def getIP():
        import network
        wlan = network.WLAN()
        return wlan.ifconfig()[0]
    
    def start():
        customnetwork.setupSTA()
    
if __name__ == '__main__':
    customnetwork.start()
""")
            fileCn.close()
            print("   ... done")
        except:
            print("ERROR: writing to file lib/customnetwork.py failed")
           
        try:
            print("   ... writing to boot.py")
            fileBoot = open('boot.py', 'w')
            fileBoot.write("""# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

try:
    from customnetwork import customnetwork
    customnetwork.start()
    del customnetwork
    gc.collect()
except:
    print("error in boot.py")
""")
            fileBoot.close()
            print("   ... done")
        except:
            print("ERROR: writing to file boot.py failed")
        
        print("Program finished.")
    else:
        print("Aborting program.")
else:
    print("Aborting program.")

