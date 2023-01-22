import rp2
import network
import time
import ubinascii


class Wifi:
    
    def __init__(self, ssid, password ):
        
        self.ssid = ssid
        self.password = password
        self.ip = None
        self.mac = None
    def __str__(self):
        return f"""-- Network settings -- 
Wifi SSID: {self.ssid}
IP Addr: {self.ip}
Mac Addr: {self.mac}
Net Mask: XXXX
DHCP: XXXX 
DNS Server: XXXX
Status: { "Connected" if self.wlan.isconnected() else "Disconnected"}"""
    def connect(self, powersavingmode = True):
        
        print("Connecting to:",self.ssid)
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(False)
        time.sleep(1)
        self.wlan.active(True)
        if not powersavingmode:
            self.wlan.config(pm = 0xa11140)
        
        self.wlan.connect(self.ssid, self.password)
        print('Waiting for WiFi connection...')
        while True:
            wstat= self.wlan.status()
            if wstat < 0 or wstat >= 3:
                break
            time.sleep(1)
        self.is_connected = self.wlan.isconnected()
        print("Connected:", self.is_connected)
        if self.is_connected:
            status = self.wlan.ifconfig()
            self.ip = status[0]
            self.mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
        return self.is_connected
    def getconfig(self):
        #Todo: Read the network settings and return them as a dataclass
        pass