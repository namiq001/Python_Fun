from scapy.all import sniff

# Paketləri işləyəcək funksiya
def packet_callback(packet):
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src   # Mənbə IP ünvanı
        ip_dst = packet["IP"].dst   # Təyinat IP ünvanı
        print(f"Packet from {ip_src} to {ip_dst}")

# Şəbəkə üzərindəki TCP paketlərini izləyirik
print("Sniffing TCP packets...")
sniff(filter="tcp", prn=packet_callback, count=10)  # 10 TCP paketini sniffləyir
