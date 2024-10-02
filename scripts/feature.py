import subprocess


def make_rules_persistent():
    """Make firewall rules persistent."""
    try:
        # Save current iptables rules
        with open("/etc/iptables/rules.v4", "w") as rules_file:
            subprocess.run(["iptables-save"], stdout=rules_file)
        print("Firewall rules have been made persistent.")
    except Exception as e:
        print(f"Error making rules persistent: {e}")


def start_daemon():
    """Start the firewall daemon."""
    try:
        # Start iptables service as a daemon
        command = ["systemctl", "start", "iptables"]
        subprocess.run(command, check=True)
        print("Firewall daemon started.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting the daemon: {e}")


if __name__ == "__main__":
    pass
