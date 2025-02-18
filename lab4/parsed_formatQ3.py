from netmiko import Netmiko

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]
for device in devices:
    print(f"Connecting to ({device['ip']})")
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show ip route", use_textfsm=True)
    net_connect.disconnect()
    print(f"Routing Information on {device['ip']}:")
    for route in output:
        protocol = route.get('protocol', 'N/A')
        network = route.get('network', 'N/A')
        distance = route.get('distance', 'N/A')
        metric = route.get('metric', 'N/A')
        print(f"  Protocol: {protocol}, Network: {network}, Distance: {distance}, Metric: {metric}")
    print("\n")
