
import os

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
