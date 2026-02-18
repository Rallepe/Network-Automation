import getpass
import telnetlib

f = open("myswitches")


user = input("Enter your telnet username: ")
password = getpass.getpass()


for IP in f:
    tn = telnetlib.Telnet(IP.strip())
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    for i in range(2, 100):
        tn.write(f"vlan {i}\n".encode('ascii'))
        tn.write(f"name Python_VLAN_{i}\n".encode('ascii'))
        tn.write(b"end\n")
        tn.write(b"exit\n") 


print(tn.read_all().decode('ascii'))