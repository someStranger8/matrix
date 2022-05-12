
import os, sys

def in_sudo_mode():
    """If the user doesn't run the program with super user privileges, don't allow them to continue."""
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()


in_sudo_mode()
clear = lambda: os.system("clear")
clear()

print(banner)

while True:
  host = input("Would you like to host a server or join one (h/j) >>> ")

  if host == "h":
    os.system("python3 server/server.py")
    break
    
  elif host == "j":
    os.system("python3 client/client.py")
    break

  else:
    print("please enter \'h\' or \'j\'")
