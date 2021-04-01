import requests
import time

while True:
    try:
        r = requests.get("https://www.google.com/")
        break
    except requests.ConnectionError:
        print("sin conexion")
        time.sleep(10)

print("Conexion")


"""
[Unit]
Description= piBot service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/verPiBot/main.py


[Install]
WantedBy=multi-user.target

"""


"""
[Unit]
Description= No Ip DUC servicio
After=network.target
After=syslog.target

[Service]
ExecStart=/usr/local/bin/noip2
type=forking
Restart=always

[Install]
WantedBy=multi-user.target
Alias=noip.service


"""