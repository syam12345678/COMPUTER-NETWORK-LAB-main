arp_table = {
    "192.168.0.1": "00-14-22-01-23-45",
    "192.168.0.2": "00-14-22-01-23-46"
}

def arp_lookup(ip):
    mac = arp_table.get(ip)
    if mac:
        print(f"ARP: MAC Address for {ip} is {mac}")
    else:
        print(f"ARP: No MAC Address found for {ip}")

# Example usage:
arp_lookup("192.168.0.1")
arp_lookup("192.168.0.10")
