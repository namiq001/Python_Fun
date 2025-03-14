from scapy.all import ARP, Ether, srp

def scan_network(network_ip):
    # Ethernet frame və ARP request yarat
    arp_request = ARP(pdst=network_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcast
    packet = ether / arp_request
    
    # Paketi göndər və cavabları al
    result = srp(packet, timeout=3, verbose=False)[0]
    
    devices = []
    for sent, received in result:
        devices.append({"IP": received.psrc, "MAC": received.hwsrc})
    
    return devices

# Şəbəkə aralığını daxil et (məsələn, 192.168.1.1-254)
network = "192.168.57.1/24"
devices = scan_network(network)

# Tapılan cihazları göstər
print("Şəbəkədə aktiv cihazlar:")
print("-" * 40)
for device in devices:
    print(f"IP: {device['IP']}\t MAC: {device['MAC']}")
