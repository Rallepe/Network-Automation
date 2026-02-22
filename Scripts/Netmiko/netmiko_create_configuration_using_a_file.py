


netmiko import ConnectHandler




iosv_l2_s1 =  {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.100',
    'username': 'david',
    'password': 'cisco',
    }

iosv_l2_s2 =  {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.101',
    'username': 'david',
    'password': 'cisco',
    }

iosv_l2_s3 =  {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.102',
    'username': 'david',
    'password': 'cisco',
    }

with open("config") as f:
    config_commands = f.read().splitlines()
print(config_commands)


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3]


for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(config_commands)
    print(output)
