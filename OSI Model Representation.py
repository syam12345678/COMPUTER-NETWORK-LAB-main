
osi_layers = {
    7: "Application - End user interface (HTTP, FTP)",
    6: "Presentation - Data translation (Encryption, Compression)",
    5: "Session - Connection management (Start/Stop Sessions)",
    4: "Transport - Reliable transmission (TCP/UDP)",
    3: "Network - Routing (IP, ICMP)",
    2: "Data Link - Error detection & framing (MAC, ARP)",
    1: "Physical - Bit transmission (Cables, Switches)"
}
print("OSI Model Layers and their Functions:\n")
for layer in sorted(osi_layers.keys(), reverse=True):
    print(f"Layer {layer}: {osi_layers[layer]}")
