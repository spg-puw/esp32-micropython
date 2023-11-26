# setup script for repo https://github.com/spg-puw/esp32-micropython/
# please execute this on your microcontroller!

def setupWifi():
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
                print("   ... creating folder lib")
                import os
                os.mkdir("lib")
                print("   ... writing to lib/customnetwork.py")
                fileCn = open('lib/customnetwork.py', 'w')
                fileCn.write("""class customnetwork:
    def setupSTA():
        import network
        import time
        import sys
        
        # default credentials
        wifi_ssid = "micropython-iot"
        if sys.platform == "esp32":
            wifi_ssid = "esp32-iot"
        elif sys.platform == "rp2":
            wifi_ssid = "rp2-iot"
        wifi_pass = "123456"
        reconnects_max = 8
        
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
            if ssid == "" or password == "": # do not continue without entries
                return
        except:
            pass
        
        wlan = network.WLAN(network.STA_IF)
        if not wlan.isconnected():
            wlan.active(True)
            macAddress = wlan.config("mac") #or machine.unique_id()
            host = "mp-" + "".join("{:02x}".format(b) for b in macAddress[3:])
            if sys.platform == "esp32":
                host = "esp32-" + "".join("{:02x}".format(b) for b in macAddress[3:])
            elif sys.platform == "rp2":
                host = "rp2-" + "".join("{:02x}".format(b) for b in macAddress[3:])
            try:
                wlan.config(hostname = host)
                wlan.config(reconnects = reconnects_max)
                wlan.config(dhcp_hostname = host)
            except:
                pass
            wlan.connect(wifi_ssid, wifi_pass)
            #wlan.ifconfig(config=('192.168.0.101', '255.255.255.0', '192.168.1.1', '8.8.8.8')) # (ip, subnet_mask, gateway, DNS_server)
            print("[wlan] trying to connect to {0} as host {1}".format(wifi_ssid, host))
            
            reconnects_num = 0
            while not wlan.isconnected() and reconnects_num < reconnects_max:
                reconnects_num += 1
                print("[wlan] trying ... [t = {}]".format(time.time()))
                time.sleep(1)
            if not wlan.isconnected():
                raise Exception("wifi connection failed - too many reconnect attempts")
        else:
            print("[wlan] board already connected to {}".format(wlan.config("essid")))
            
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
            print("[wlan] creating ap ... [{}]".format(time.time()))
            time.sleep(1)
            
        print("[wlan] ap created")
        customnetwork.printNetworkInformation()

    def printNetworkInformation(detail = False):
        import network
        wlan = network.WLAN()
        ni = wlan.ifconfig()
        print("[wlan] ----- network information -----")
        print("[wlan] Hostname: {0}".format(wlan.config("hostname")))
        print("[wlan] SSID: {0}".format(wlan.config("essid")))
        print("[wlan] IP: {0}".format(ni[0]))
        if detail == True:
            print("[wlan] Subnetmask: {0}".format(ni[1]))
            print("[wlan] Gateway: {0}".format(ni[2]))
            print("[wlan] DNS: {0}".format(ni[3]))
        print("[wlan] -------------------------------")

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
except Exception as e:
    print("error in boot.py: {0}".format(e))
finally:
    import gc
    del customnetwork
    gc.collect()
""")
                fileBoot.close()
                print("   ... done")
            except:
                print("ERROR: writing to file boot.py failed")
            
            print("Writing files finished.")
        else:
            print("Aborting program.")
    else:
        print("Aborting program.")

def setupInstallFiles():
    try:
        from customnetwork import customnetwork
        customnetwork.start()
    except:
        pass
    
    import mip
    print("start install")
    mip.install("github:spg-puw/esp32-micropython")
    print("done")

if __name__ == "__main__":
    c = input("Setup:\n   type '1' for wifi\n   type '2' to install dependencies (wifi must be connected)\n   type '3' for both\nWhich setup do you want to execute?\nPlease enter a number: ")
    if c == "1":
        setupWifi()
    elif c == "2":
        setupInstallFiles()
    elif c == "3":
        setupWifi()
        setupInstallFiles()
    else:
        print("Unknown. Exiting.")

