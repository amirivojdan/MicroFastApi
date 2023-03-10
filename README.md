# MicroFastApi

Fast MicroPython Web API Framework inpired by awesome [FastApi](https://fastapi.tiangolo.com/) project.

```python
from microfastapi import MicroFastApi
from wifi import Wifi
from secrets import *
import machine

machine.freq(133000000) # set the CPU frequency to 133 MHz(max)

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
```

```console
Connecting to: XXXXX
Waiting for WiFi connection...
Connected: True

 -- Network settings -- 
Wifi SSID: XXXXX
IP Addr: 10.0.0.67
Mac Addr: xx:xx:xx:xx:xx:xx
Net Mask: XXXX
DHCP: XXXX 
DNS Server: XXXX
Status: Connected 

API server running on http://10.0.0.67:80
client connected from ('10.0.0.30', 49992)
client closed!
```

```json
{"userId": "1"}
```