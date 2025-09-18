import subprocess
import os
import time
from colorama import Fore as f, init

# Inisialisasi Colorama
init()

# ASCII ART
print(f.LIGHTCYAN_EX + "")
print("     000000000000        000000000000000000000000000000000000000000000      ")
print("      000      000      000                                       000      ")
print("       000      0000   000    000000000000000                   6000      ")
print("        000      00000000     0000000000000000      000000000000000      ")
print("         0000      0000      000000000000000   0               0000   ")
print("          000      00      00                000                 0000000  ")
print("           000            000                  00000000000000      000 ")
print("            0000        00000     000000000     000               000 ")
print("             0000      000000     000   0000      00             000 ")
print("              0000000000  0000000000     0000000000000000000000000\n ")
print(f.LIGHTWHITE_EX + "                          WiFEX BY @versaagonon\n")
print(f.LIGHTWHITE_EX + "\n  [+] Made by @Versaagonon  [+] Instagram : @versaagonon\n")

VALIDATION_KEY = "versaagonon"

while True:
    key = input(f.LIGHTYELLOW_EX + "[>] Enter Validation Key: " + f.LIGHTCYAN_EX)
    if key == VALIDATION_KEY:
        print(f.LIGHTGREEN_EX + "[✔] Validation key true! Starting the program...\n")
        break
    else:
        print(f.LIGHTRED_EX + "[✘] Validation key wrong! Try again...\n")
def get_wifi_profiles():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    return profiles

def get_wifi_details(profile):
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')

    ssid = [e.split(":")[1][1:-1] for e in results if "SSID name" in e]
    auth = [c.split(":")[1][1:-1] for c in results if "Authentication" in c]
    cipher = [d.split(":")[1][1:-1] for d in results if "Cipher" in d]
    password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    return ssid[0] if ssid else "N/A", auth[0] if auth else "N/A", cipher[0] if cipher else "N/A", password[0] if password else "no detected"

print(f.LIGHTGREEN_EX + "\n+--------------------+-------------------+------------------+---------------+----------------+")
print("|       Name        |        SSID       |  Authentication  |  Encryption   |    Password    |")
print("+--------------------+-------------------+------------------+---------------+----------------+")

for profile in get_wifi_profiles():
    ssid, auth, cipher, password = get_wifi_details(profile)
    print(f.LIGHTYELLOW_EX + "| {:<18} | {:<17} | {:<16} | {:<13} | {:<14} |".format(profile, ssid, auth, cipher, password))
    print(f.LIGHTGREEN_EX + "+--------------------+-------------------+------------------+---------------+----------------+")

print(f.LIGHTGREEN_EX + "\n[✔] Process done!\n")

input("\n[>] Press Enter to exit...")
