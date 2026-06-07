import network
import time

#zoekt verbingen met wifi
def connect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        print("...")
        time.sleep(1)

    print(wlan.ifconfig()[0])
    return wlan
