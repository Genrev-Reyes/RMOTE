from zipfile import ZipFile
from os import system
from os.path import isfile
from time import sleep
import sys
#Extract web Files
with ZipFile(".web.zip", "r") as File:
    File.extractall("/root/RMOTE")

# Remove web zip


# Install Modules

Modules = ("bs4", "requests", "rich")
system("pip3 install bs4")
system("pip3 install requests")
system("pip3 install rich")

# Install Packages

Termux = "/data/data/com.termux/files/home/RMOTE/Rmote.py"
Linux = "/root/RMOTE/Rmote.py"
Termux_adb = "android-tools"
Linux_adb = "wireless-tools adb"
if isfile(Termux):
    system("pkg install ssh")
    system("pkg install android-tools")
    system("pkg install nmap")
    system("clear")
    sleep(1)
    print("[+] Succesfully Installed")
if isfile(Linux):
    system("sudo apt-get install wireless-tools adb")
    system("sudo apt-get install nmap")
    system("sudo apt-get install ssh")
    system("clear")
    sleep(1)
    print(" [+] Succesfully Installed")
