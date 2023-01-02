#find the MAC address of a specific network interface, example finds the MAD address of the eth0 interface

import netifaces

def get_interface_mac_address(interface):
    #get MAC address of the specified interface
    if_addrs = netifaces.ifaddress(interface)
    if netifaces.AF_LINK in if_addrs:
        link_layer_info = if_addrs[netifaces.AF_LINK]
        if link_layer_info:
            mac_address = link_layer_info[0]['addr']
            return mac_address

eth0_mac_address = get_interface_mac_address('eth0')
print('{eth0_mac_address}')
