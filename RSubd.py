# =============================================================================
#                       RSubd www.github.com/wrrulos
#                   Script to scan subdomains of a domain
#                            Made by wRRulos
#                               @wrrulos
# =============================================================================

# Any error report it to my discord please, thank you.
# Programmed in Python 3.10.1
# Discord: Rulo#9224

import socket
import os

from argparse import ArgumentParser
from colorama import Fore, init

init()

number_of_lines = 0
ips_list = []
domain = ""
file = ""
skip_ip = ""
logs_file = ""
os_name = ""


# Colors

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET

# Banners

banner = f"""{white}
 {lyellow} _____   _____       _         _ 
 {lyellow}|  __ \ / ____|     | |       | |    {white}$ {lgreen}google.com{white}  ___ @ {lyellow}ftp.{lgreen}google.com{reset} 
 {lyellow}| |__) | (___  _   _| |__   __| |                 {white}|
 {lyellow}|  _  / \___ \| | | | '_ \ / _` |                 {white}|___ @ {lyellow}www.{lgreen}google.com{reset}
 {lyellow}| | \ \ ____) | |_| | |_) | (_| |                 {white}|   
 {lyellow}|_|  \_\_____/ \__,_|_.__/ \__,_|                 {white}|___ @ {lyellow}admin.{lgreen}google.com{reset} 
            
     Version: 1.0 By wRRulos                     
"""

termux_banner = f"""{white}
 {lyellow} _____   _____       _         _ 
 {lyellow}|  __ \ / ____|     | |       | |
 {lyellow}| |__) | (___  _   _| |__   __| |  
 {lyellow}|  _  / \___ \| | | | '_ \ / _` |
 {lyellow}| | \ \ ____) | |_| | |_) | (_| |  
 {lyellow}|_|  \_\_____/ \__,_|_.__/ \__,_|  
            
 Version: 1.0 By wRRulos (Termux Edition)"""


def check_os():
    """
    Detect the operating system
    """

    global os_name

    if os.name == "nt":
        os_name = "Windows"

    else:
        if os.path.exists("/data/data/com.termux/files/home"):
            os_name = "Termux"

        else:
            os_name = "Linux"


def clear():
    """
    Clean the screen
    """
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")


def check_connection():
    """
    Check if you have an internet connection
    """
    try:
        socket.gethostbyname("google.com")

    except:
        print("You need to be connected to the internet")
        exit()


def check_domain():
    """
    Check domain
    """
    try:
        socket.gethostbyname(domain)

    except:
        print("Enter a valid domain!")
        exit()


def check_file():
    """
    Check file
    """
    if os.path.exists(file):
        pass

    else:
        print("File not found!")
        exit()


def check_arguments():
    """
    Check the arguments
    """
    global domain
    global file
    global skip_ip
    global logs_file

    parser = ArgumentParser(description='Script to scan subdomains of a domain')
    parser.add_argument("-d", help="Domain", required=True, action="store", dest="domain")
    parser.add_argument("-l", help="List of subdomains", required=True, action="store", dest="file")
    parser.add_argument("-s", help="Skip subdomains with the same ip", default="n", dest="skip_ip", action="store_true")
    parser.add_argument("-sv", help="Save the results to a file", default="n", dest="logs_file", action="store")
    args = parser.parse_args()

    domain = args.domain
    file = args.file
    skip_ip = args.skip_ip
    logs_file = args.logs_file

    check_domain()
    check_file()


def scan():
    """
    Scan the domain
    """
    global number_of_lines
    global ips_list

    logs = ""
    num = 0

    with open(file) as f:
        for line in f:
            number_of_lines += 1

    if not logs_file == "n":  # If the user uses the "-sv" parameter
        if not os.path.exists(logs_file):
            logs = open(logs_file, "w", encoding="utf8")  # Save logs
            logs.write(f"Scanning the domain {domain}\n\nFile: {file} ({number_of_lines} subdomains)\n")

            if not skip_ip == "n":  # If the user uses the "-s" parameter
                logs.write("Skip subdomains with the same ip: Yes\n")

            else:
                logs.write("Skip subdomains with the same ip: No\n")

        else:
            print("A file with that name already exists!")
            exit()

    clear()

    if os_name == "Termux":
        print(f"\n{termux_banner}\n\n Scanning the domain {lgreen}{domain}{white}..\n\n File: {file} ({number_of_lines} subdomains)")

    else:
        print(f"\n{banner}\n\n Scanning the domain {lgreen}{domain}{white}..\n\n File: {file} ({number_of_lines} subdomains)")

    if not skip_ip == "n":  # If the user uses the "-s" parameter
        print(" Skip subdomains with the same ip: Yes\n", end="")

    else:
        print(" Skip subdomains with the same ip: No\n", end="")

    if not logs_file == "n":  # If the user uses the "-sv" parameter
        print(f" Log file: {logs_file}\n")

    else:
        pass

    with open(file) as f:
        for line in f:
            line_subdomain = line.split("\n")

            try:
                subdomain = f"{str(line_subdomain[0])}.{str(domain)}"
                ip_subdomain = socket.gethostbyname(subdomain)

                if not skip_ip == "n":  # If the user uses the "-s" parameter

                    if str(ip_subdomain) not in ips_list:
                        ips_list.append(str(ip_subdomain))
                        num += 1

                        if os_name == "Termux":
                            print(f" {white}Found! {lblack}» {lyellow}{str(subdomain)} {lblack}{str(ip_subdomain)}")

                            if not logs_file == "n":  # If the user uses the "-sv" parameter
                                logs.write(f"\nSubdomain found » {str(subdomain)} {str(ip_subdomain)}")

                        else:
                            print(f" {white}Subdomain found {lblack}» {lyellow}{str(subdomain)} {lblack}{str(ip_subdomain)}")

                            if not logs_file == "n":  # If the user uses the "-sv" parameter
                                logs.write(f"\nSubdomain found » {str(subdomain)} {str(ip_subdomain)}")

                else:
                    num += 1

                    if os_name == "Termux":
                        print(f" {white}Found! {lblack}» {lyellow}{str(subdomain)} {lblack}{str(ip_subdomain)}")

                        if not logs_file == "n":  # If the user uses the "-sv" parameter
                            logs.write(f"\nSubdomain found » {str(subdomain)} {str(ip_subdomain)}")

                    else:
                        print(f" {white}Subdomain found {lblack}» {lyellow}{str(subdomain)} {lblack}{str(ip_subdomain)}")

                        if not logs_file == "n":  # If the user uses the "-sv" parameter
                            logs.write(f"\nSubdomain found » {str(subdomain)} {str(ip_subdomain)}")
            except:
                pass

    print(f"\n{white} The scan finished and found {green}{num} {white}subdomains")

    if not logs_file == "n":  # If the user uses the "-sv" parameter
        logs.close()


if __name__ == "__main__":
    print("")
    check_os()
    check_arguments()
    check_connection()
    scan()
