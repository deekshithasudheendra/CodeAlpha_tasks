from scapy.all import *

def packet_callback(packet):
    print("\n=== Packet Captured ===")

    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

    print(packet.summary())

print("Starting Network Sniffer...")
print("Press Ctrl + C to stop.\n")

sniff(prn=packet_callback, store=False)

input("Press Enter to exit...")