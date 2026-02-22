from netmiko import ConnectHandler


iosv_l2 =  {
    'device_type': 'cisco_ios',
    'ip': '192.168.255.100',
    'username': 'david',
    'password': 'cisco',
    }

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)


for n in range(2, 21):
    print(f'Creating VLAN {n}')
    config_commands = [f'vlan {n}', f'Python_VLAN_{n}']
    output = net_connect.send_config_set(config_commands)
    print(output)