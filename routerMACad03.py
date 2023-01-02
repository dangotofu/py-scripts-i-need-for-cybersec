import subprocess

def get_router_mac_address():
    arp_output = subprocess.run(['arp', '-a'], capture_output = True)stdout.decode()

    lines = arp_output.split('\n')

    for line in lines:
        #could also be 192.168.1.1
        if '192.168.0.1' in line:
            router_mac = line.split()[1]
            return router_mac

router_mac = get_router_mac_address()
print('{router_mac}')
