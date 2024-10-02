"""
--------------------------------- FIREWALL ---------------------------------

This file contains the core functions used by the firewall to block or unblock incoming requests.
The methods can block packets based on IP, MAC, PORT, and PROTOCOL, and also provide validation.

----------------------------------- END ------------------------------------
"""

# Required modules for creating the core functionality of the firewall
import logging
import subprocess

from . import validation as val

# LOGGING FEATURE'S BASIC CONFIGURATION
# Configure the dedicated logger for firewall actions
firewall_logger = logging.getLogger("firewall_logger")
firewall_logger.setLevel(logging.INFO)

# Create a file handler that logs to 'firewall_actions.log'
fh = logging.FileHandler("firewall_actions.log")
fh.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

# Add the handler to the logger
firewall_logger.addHandler(fh)

"""
BLOCKING FUNCTIONS 

This block contains the functions that block packets based on IP, MAC, PORT, and PROTOCOL.
"""


# IP BLOCKER
def block_ip(ip_address):
    """Blocks an IP address."""
    if not val.is_valid_ip(ip_address):
        return "Invalid IP address"

    try:
        command = f"iptables -A INPUT -s {ip_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked IP address {ip_address}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block IP address {ip_address}: {e}"
        return error_message


def block_mac(mac_address):
    """Blocks a MAC address after validation."""
    if not val.is_valid_mac(mac_address):
        return "Invalid MAC address"

    try:
        command = f"iptables -A INPUT -m mac --mac-source {mac_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked MAC address {mac_address}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block MAC address {mac_address}: {e}"
        return error_message


def block_port(port):
    """Blocks a specific port for incoming connections."""
    if not val.is_valid_port(port):
        return "Invalid port"

    try:
        command = (
            f"iptables -A INPUT -p tcp --dport {port} -j DROP; "
            f"iptables -A INPUT -p udp --dport {port} -j DROP; "
            f"iptables -A OUTPUT -p tcp --dport {port} -j DROP; "
            f"iptables -A OUTPUT -p udp --dport {port} -j DROP;"
        )
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked incoming requests on port {port}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block incoming requests on port {port}: {e}"
        return error_message


def block_protocol(protocol):
    """Blocks all traffic for a specific protocol (TCP, UDP, etc.)."""
    if not val.is_valid_protocol(protocol):
        return "Invalid protocol"

    try:
        command = (
            f"iptables -A INPUT -p {protocol} -j DROP; "
            f"iptables -A OUTPUT -p {protocol} -j DROP"
        )
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked protocol {protocol}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block protocol {protocol}: {e}"
        return error_message


"""
UNBLOCKING FUNCTIONS

This block contains functions used to remove the rules from the table.
"""


def unblock_ip(ip_address):
    """Removes block on an IP address."""
    if not val.is_valid_ip(ip_address):
        return "Invalid IP address"

    try:
        command = f"iptables -D INPUT -s {ip_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked IP address {ip_address}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock IP address {ip_address}: {e}"
        return error_message


def unblock_mac(mac_address):
    """Removes block on a MAC address."""
    if not val.is_valid_mac(mac_address):
        return "Invalid MAC address"

    try:
        command = f"iptables -D INPUT -m mac --mac-source {mac_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked MAC address {mac_address}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock MAC address {mac_address}: {e}"
        return error_message


def unblock_port(port):
    """Removes block on a specific port for incoming connections."""
    if not val.is_valid_port(port):
        return "Invalid port"

    try:
        command = (
            f"iptables -D INPUT -p tcp --dport {port} -j DROP; "
            f"iptables -D INPUT -p udp --dport {port} -j DROP; "
            f"iptables -D OUTPUT -p tcp --dport {port} -j DROP; "
            f"iptables -D OUTPUT -p udp --dport {port} -j DROP;"
        )
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked incoming requests on port {port}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock incoming requests on port {port}: {e}"
        return error_message


def unblock_protocol(protocol):
    """Removes block on a specific protocol."""
    if not val.is_valid_protocol(protocol):
        return "Invalid protocol"

    try:
        command = (
            f"iptables -D INPUT -p {protocol} -j DROP; "
            f"iptables -D OUTPUT -p {protocol} -j DROP"
        )
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked protocol {protocol}"
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock protocol {protocol}: {e}"
        return error_message


""" RESET BUTTON TO FLUSH ALL THE RULES """


def reset_rule():

    try:
        command = f"iptables -F"
        subprocess.run(command, shell=True, check=True)
        message = f"All rules has been reset ..."
        firewall_logger.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to reset the rules: {e}"
        return error_message
