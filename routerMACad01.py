import platform

def get_router_mac_address():
    default_gateway = platform.node()
    mac_address = uuid.getnode()
    return mac_address

router_mac_address = get_router_mac_address()
print('{router_mac_address}')
