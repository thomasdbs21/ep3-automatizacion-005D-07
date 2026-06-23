from ncclient import manager

with manager.connect(
    host="192.168.199.4",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False,
    device_params={"name": "iosxe"},
    allow_agent=False,
    look_for_keys=False
) as router:

    filtro = """
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname/>
      </native>
    </filter>
    """

    respuesta = router.get_config("running", filtro)

    print(respuesta.xml)

    with open("evidencias/rpc_reply_raw.xml", "w") as archivo:
        archivo.write(respuesta.xml)
