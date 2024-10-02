# Firewall Web Interface

This project is a Python-based firewall with a web interface built using Flask. It allows users to manage firewall rules, including blocking and unblocking IP addresses, MAC addresses, ports, and protocols (TCP/UDP). It provides a user-friendly dashboard for managing firewall rules, and features authentication and logging for security and traceability.

This project is built using Python as the core scripting language, along with the Linux utility `iptables` for managing firewall rules. The frontend is developed using Flask, a lightweight Python web framework, providing a user-friendly interface for firewall management. Flask handles the web interface, allowing users to easily manage IP, MAC, port, and protocol-based rules through the dashboard. The integration of Python and `iptables` ensures robust firewall functionality, while Flask adds simplicity and flexibility to the user experience. This combination offers a powerful and efficient firewall solution.

## Features

- **IP Blocking/Unblocking**: Block and unblock IP addresses.
- **MAC Address Blocking/Unblocking**: Block and unblock MAC addresses.
- **Port Blocking/Unblocking**: Block and unblock specific ports.
- **Protocol Filtering**: Block and unblock protocols (TCP/UDP).
- **Authentication**: Secure login and password management with hashed passwords.
- **Logging**: Detailed logging of firewall actions (block/unblock commands) in a separate log file.

## Installation

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- Flask
- `iptables` (or an equivalent for managing firewall rules)

### Setting Up

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kishore-001/firewall.git
   cd firewall

2. **Set up virtual environment:**

    It is recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install the package and dependencies:**

    Run the following command to install the firewall app and its dependencies using the `setup.py` script:
    ```bash
    sudo python3 setup.py install

4. **Create initial user**

    When running the firewall for the first time, you will need to create an admin user. Start the app and it will prompt you to create a new user with a hashed password.

5. **Run the application**

    To start the web interface:

    ```bash
    sudo python3 app.py
    ```

    This will start the Flask server. Open a browser and navigate to http://127.0.0.1:5000 to access the firewall dashboard.



## Note

- **Use sudo** when running the app to ensure the proper permissions for applying firewall rules (e.g., IP blocking).
- The web interface should be accessed via the browser at http://127.0.0.1:5000.

## Logs

- **Firewall actions** (block/unblock IPs, MACs, Ports, etc.) are logged in `firewall_actions.log` located in the root directory.
- This ensures traceability of firewall changes, and logs are kept clean without including unnecessary web server details.

## Usage

- **Dashboard**: Use the dashboard to manage IP, MAC, port, and protocol-based rules.
- **Logs**: Check the logs for detailed information on all firewall changes.
- **Authentication**: Login is required to access the firewall management page. Secure password hashing is used for password storage.

## Contributing

Feel free to contribute by submitting issues or pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

