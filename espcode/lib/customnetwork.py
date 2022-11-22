def setupSTA():
    import network
    import time
    import wificonfig
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        macAddress = wlan.config("mac") #or machine.unique_id()
        host = "esp32-" + "".join("{:02x}".format(b) for b in macAddress[3:])
        wlan.config(dhcp_hostname = host)
        wlan.connect(wificonfig.STA.ssid, wificonfig.STA.password)
        #wlan.ifconfig(config=('192.168.0.101', '255.255.255.0', '192.168.0.1', '8.8.8.8')) # (ip, subnet_mask, gateway, DNS_server)
        print("trying to connect to {0} as host {1}".format(wificonfig.STA.ssid, host))
        while not wlan.isconnected():
            print("trying ... [{}]".format(time.time()))
            time.sleep(1)
            #machine.idle()
    else:
        print("board already connected to {}".format(wlan.config("essid")))
        
    print("network inforomation:", wlan.ifconfig()) #network info for debugging
    ip = wlan.ifconfig()[0]

def setupAP():
    import network
    import time
    import wificonfig
    wlan = network.WLAN(network.AP_IF)
    wlan.active(True)
    wlan.config(essid = wificonfig.AP.ssid, password = wificonfig.AP.password)
    
    while wlan.active() == False:
        print("creating ap ... [{}]".format(time.time()))
        time.sleep(1)
    print("ap created")
    print("network inforomation:", wlan.ifconfig()) #network info for debugging
    ip = wlan.ifconfig()[0]

def getIP():
    import network
    wlan = network.WLAN()
    return wlan.ifconfig()[0]
    
if __name__ == '__main__':
    setupSTA()