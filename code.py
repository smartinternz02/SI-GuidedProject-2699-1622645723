import wiotp.sdk.device
import time
import random
from pHcalc.pHcalc import Acid, Neutral, System
myConfig = { 
    "identity": {
        "orgId": "kzz9wo",
        "typeId": "externship",
        "deviceId":"200102"
    },
    "auth": {
        "token": "23456789"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    print()
    
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(0,125)
    hum=random.randint(0,100)
    PH=random.randint(0,14)
    myData={'d':{'temperature':temp, 'humidity':hum, 'pHvalue':PH}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    print()
    if temp<50 and hum<20:
        print("Everything is fine,water can be used")
    elif temp>50 and hum>20:
        print("Entering danger zone,The Hay is too wet")
    elif temp>75:
        print("HIGH ALERT is required")
    elif PH>6.5 and PH<8.5:
        print("water can be drunk")
    else:
        print("PH of water is not suitable for drinking")
    print()
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
