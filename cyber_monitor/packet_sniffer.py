from scapy.all import sniff

def packet_callback(packet):
    print(f"Packet Captured: {packet.summary()}")

def start_sniffing():
    print("Sniffing started...")
    sniff(prn=packet_callback, count=10)
