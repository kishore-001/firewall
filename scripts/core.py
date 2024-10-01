"""
--------------------------------- FIREWALL ---------------------------------

This file contains the core function which the firewall used to block or remove the incoming request .
The methods can block packet based on IP, MAC, PORT, PROTOCAL which also provide the validation 

----------------------------------- END ------------------------------------
"""

# Below are the required modules which will be used to create the core fucntionality of the firewall

import logging
import subprocess

from validation import *

# LOGGING FEATURE's BASIC CONFIGURATION

logging.basicConfig(
    filename="firewall.log",  # Log to a file named 'firewall.log'
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


"""
BLOCKING FUNCTIONS 

      -> This block contains the blocking function based on IP, MAC, PORT, PROTOCAL ....

"""

# IP BLOCKER


def block_ip(ip_address):
    """Blocks an IP address."""

    if not is_valid_ip(ip_address):
        # invalid_input()
        pass

    try:
        command = f"iptables -A INPUT -s {ip_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked IP address {ip_address}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block IP address {ip_address}: {e}"
        logging.error(error_message)
        # guierror()


def block_mac(mac_address):
    """Blocks a MAC address after validation."""

    if not is_valid_mac(mac_address):
        # invalid_input()
        pass

    try:
        command = f"iptables -A INPUT -m mac --mac-source {mac_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked MAC address {mac_address}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block MAC address {mac_address}: {e}"
        logging.error(error_message)
        return error_message


def block_port(port):
    """Blocks a specific port for incoming connections."""

    if not is_valid_port(port):
        # invalid_input()
        pass

    try:
        command = f"iptables -A INPUT -p tcp --dport {port} -j DROP;iptables -A INPUT -p udp --dport {port} -j DROP;iptables -A OUTPUT -p tcp --dport {port} -j DROP;iptables -A OUTPUT -p udp --dport {port} -j DROP;"
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked incoming requests on port {port}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block incoming requests on port {port}: {e}"
        logging.error(error_message)
        return error_message


def block_protocol(protocol):
    """Blocks all traffic for a specific protocol (TCP, UDP, etc.)."""

    if not is_valid_protocol(protocol):
        # invalid_input()
        pass

    try:
        command = f"iptables -A INPUT -p {protocol} -j DROP;iptables -A OUTPUT -p {protocol} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Blocked protocol {protocol}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to block protocol {protocol}: {e}"
        logging.error(error_message)
        return error_message


"""
UNBLOCKING FUNCTIONS

        -> This contains functios which is used to remove the rules from the table
"""


def unblock_ip(ip_address):
    """Removes block on an IP address."""

    if not is_valid_ip(ip_address):
        pass
        # invalid_input()

    try:
        command = f"iptables -D INPUT -s {ip_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked IP address {ip_address}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock IP address {ip_address}: {e}"
        logging.error(error_message)
        return error_message


def unblock_mac(mac_address):
    """Removes block on a MAC address."""
    if not is_valid_mac(mac_address):
        pass
        # invalid_input()

    try:
        command = f"iptables -D INPUT -m mac --mac-source {mac_address} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked MAC address {mac_address}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock MAC address {mac_address}: {e}"
        logging.error(error_message)
        return error_message


def unblock_port(port):
    """Removes block on a specific port for incoming connections."""

    if not is_valid_port(port):
        pass
        # invalid_input()

    try:
        command = f"iptables -D INPUT -p tcp --dport {port} -j DROP;iptables -D INPUT -p udp --dport {port} -j DROP;iptables -D OUTPUT -p tcp --dport {port} -j DROP;iptables -D OUTPUT -p udp --dport {port} -j DROP;"
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked incoming requests on port {port}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock incoming requests on port {port}: {e}"
        logging.error(error_message)
        return error_message


def unblock_protocol(protocol):
    """Removes block on a specific protocol."""

    if not is_valid_protocol(protocol):
        pass
        # invalid_input()

    try:
        command = f"iptables -D INPUT -p {protocol} -j DROP;iptables -D OUTPUT -p {protocol} -j DROP"
        subprocess.run(command, shell=True, check=True)
        message = f"Unblocked protocol {protocol}"
        logging.info(message)
        return message
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to unblock protocol {protocol}: {e}"
        logging.error(error_message)
        return error_message
