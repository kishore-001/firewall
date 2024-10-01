import re

# here contains the funcion which is used for validation ...

"""Validates the MAC address format."""


def is_valid_mac(mac_address):
    mac_pattern = r"^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$"
    return re.match(mac_pattern, mac_address) is not None


"""Validates an IPv4 address."""


def is_valid_ip(ip_address):
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if re.match(ip_pattern, ip_address):
        parts = ip_address.split(".")
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False


"""Validates if the port is in the valid range (1-65535)."""


def is_valid_port(port):
    port = int(port)
    return 1 <= port <= 65535


"""Validates if the protocol is either TCP, UDP, or ICMP."""


def is_valid_protocol(protocol):
    valid_protocols = ["tcp", "udp", "icmp"]
    return protocol.lower() in valid_protocols
