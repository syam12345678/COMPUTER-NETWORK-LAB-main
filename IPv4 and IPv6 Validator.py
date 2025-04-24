import ipaddress
def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if isinstance(ip_obj, ipaddress.IPv4Address):
            print(f"{ip} is a valid IPv4 address.")
        else:
            print(f"{ip} is a valid IPv6 address.")
    except ValueError:
        print(f"{ip} is not a valid IP address.")

validate_ip("192.168.0.1")
validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
validate_ip("123.456.789.000")
