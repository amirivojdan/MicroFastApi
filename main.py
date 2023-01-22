from microfastapi import MicroFastApi
from wifi import Wifi
from secrets import *

import machine

print(machine.freq())          # get the current frequency of the CPU
machine.freq(133000000) # set the CPU frequency to 133 MHz(max)
print(machine.freq())

wifihandle = Wifi(ssid = ssid, password = password)

if not wifihandle.connect(powersavingmode=False):
    raise Exception("Connection failed!")

print("\n",wifihandle,"\n")

app = MicroFastApi(ip= wifihandle.ip, port=80, mac= wifihandle.mac)
    
@app.get('/')
def index():
    return {'userId': 1}   

@app.get('/sensors/')
def sensors(userId:int=None):
    return {'userId':'1'}

app.Run()