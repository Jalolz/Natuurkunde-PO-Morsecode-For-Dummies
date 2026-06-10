import socket
import time
from machine import Pin
from wifi import connect
from html_page import html
from morsecode import get_morse

#wifi gegevens
SSID = ""
PASSWORD = ""

#wifi zoeken
wlan = connect(SSID, PASSWORD)
ip = wlan.ifconfig()[0]

#led raspberry pi
led = Pin("LED", Pin.OUT)

#dot en dash gegevens
def blink_morse(code):
    for symbol in code:
        if symbol == ".":
            led.on()
            time.sleep(0.2)
        elif symbol == "-":
            led.on()
            time.sleep(0.6)
        led.off()
        time.sleep(0.2)
    time.sleep(0.6)

#wifi gevonden
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip, 80))
s.listen(1)
print(f"http://{ip}:80")

pending_letter = None

#stuurt letter naar server
try:
    while True:
        conn, addr = s.accept()
        request = conn.recv(1024).decode()
        
        time.sleep(.5)

        if "/letter?char=" in request:
            start = request.find("/letter?char=") + 13
            letter = request[start]
            pending_letter = letter
            conn.send("HTTP/1.1 200 OK\r\n")
            conn.send("Content-Type: text/plain\r\n\r\n")
            conn.send("OK")
        else:
            conn.send("HTTP/1.1 200 OK\r\n")
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.sendall(html)
        conn.close()

        if pending_letter:
            code = get_morse(pending_letter)
            if code:
                blink_morse(code)
            pending_letter = None

#zorgt ervoor bij een blind close of afsluiting dat het niet currupt gaat.
except KeyboardInterrupt:
    print("Server Quit")
finally:
    s.close()

