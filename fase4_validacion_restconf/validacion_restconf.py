import requests
import json

url = "https://192.168.199.4/restconf/data/Cisco-IOS-XE-native:native/hostname"

respuesta = requests.get(
    url,
    auth=("cisco", "cisco123!"),
    headers={"Accept": "application/yang-data+json"},
    verify=False
)

print(json.dumps(respuesta.json(), indent=4))

with open("evidencias/responses/hostname.json", "w") as archivo:
    json.dump(respuesta.json(), archivo, indent=4)
