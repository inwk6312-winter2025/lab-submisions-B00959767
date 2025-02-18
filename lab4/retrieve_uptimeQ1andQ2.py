from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",  # Router 1
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",  # Router 2
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",  # Router 3
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": "22",
    },
]

for device in devices:
    print(f"\nConnecting to {device['ip']}...")
    net_connect = Netmiko(**device)
    net_connect.enable()
    
    # Retrieve uptime
    output = net_connect.send_command("show version")
    uptime_index = output.find('uptime is')
    if uptime_index != -1:
        uptime = output[uptime_index:uptime_index + 38]
        print(f"[+] {device['ip']} Uptime: {uptime}")
    else:
        print(f"[-] Uptime information not found for {device['ip']}")
    
    # Retrieve Configuration Register
    config_reg_index = output.find('Configuration register is')
    if config_reg_index != -1:
        config_reg = output[config_reg_index:].splitlines()[0]
        print(f"[+] {device['ip']} Config Register: {config_reg}")
    else:
        print(f"[-] Configuration Register not found for {device['ip']}")
    
    # Retrieve Running Configuration
    running_config = net_connect.send_command("show running-config")
    print(f"[+] {device['ip']} Running Config:\n{running_config[:500]}...")  # Show only first 500 characters
    
    net_connect.disconnect()
    print("Disconnected.")
    print("=" * 50)
