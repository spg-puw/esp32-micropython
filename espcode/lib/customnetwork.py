class customnetwork:
    def setupSTA():
        import network
        import time
        
        # default credentials
        wifi_ssid = "esp32-iot"
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
            host = "esp32-" + "".join("{:02x}".format(b) for b in macAddress[3:])
            wlan.config(dhcp_hostname = host)
            wlan.config(reconnects = reconnects_max)
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
