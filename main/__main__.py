
import os, sys

def in_sudo_mode():
    """If the user doesn't run the program with super user privileges, don't allow them to continue."""
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()


in_sudo_mode()
clear = lambda: os.system("clear")
os.system("sudo apt install netcat -y")
clear()


print("hello")
print("")
print("enter 1 to host a server or 2 to join one")
host=input("or 3 for global chat >>> ")


if host == "1":
     clear()
     print("server ip:")
     os.system("hostname -i")
     print("server status: online")
     print("")
     os.system("nc -lp 4444")


elif host == "2":
     ip=input("enter server ip >>> ")
     clear()
     print("connected to server")
     print("")
     os.system("nc "+ ip+" 4444")


elif host == "3":
    clear()
    os.system("python3 client.py 192.168.55.13 8081")
