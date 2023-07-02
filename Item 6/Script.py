import requests
import netmiko
import json
from netmiko import ConnectHandler

cisco1 = {
    "ip": "172.30.33.147",
    "device_type": "cisco_ios",
    "username": "cisco",
    "password": "cisco123!",
}

# Comando "show" que ejecutamos.
command = "show run"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Limpia automáticamente la salida para que solo se devuelva la salida del comando "show".
print()
print(output)
print()

