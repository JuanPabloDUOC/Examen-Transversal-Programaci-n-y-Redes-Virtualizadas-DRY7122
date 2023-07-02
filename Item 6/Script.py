import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = {
    "ip": "131.226.217.149",
    "device_type": "cisco_ios",
    "username": "developer",
    "password": "lastorangerestoreball8876",
}

# Comando "show" que ejecutamos.
#command = "sh ip int brief"
#command = "sh run"
command = "sh ver"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Limpia automáticamente la salida para que solo se devuelva la salida del comando "show".
print()
print(output)
print()

