import getpass
import telnetlib

HOST = "192.168.255.101"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
for i in range(1, 101):
    tn.write(f"vlan {i}\n")
    tn.write(f"name Python_VLAN_{i}\n")

tn.write(b"end\n")
tn.write(b"exit\n") 


print(tn.read_all().decode('ascii'))