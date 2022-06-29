import os
import urllib.request as urllib2
import urllib.error
import json


print('''                 ___ ____     _____               _
                |_ _|  _ \   |_   _| __ __ _  ___| | _____ _ __
                 | || |_) |____| || '__/ _` |/ __| |/ / _ \ '__|
                 | ||  __/_____| || | | (_| | (__|   <  __/ |
                |___|_|        |_||_|  \__,_|\___|_|\_\___|_|

''')

print("[1] Track an IP address")
print("[2] Exit")
print("\n")
opt = input("IP-Tracker@root: ")
opt = int(opt)
if opt == 1:
    url = "http://ip-api.com/json/"
    print("\n")
    ip = input("[+] Target IP: ")
    res = urllib2.urlopen(url + ip)
    data = res.read()
    values = json.loads(data)
    print("\n")
    print("[+] IP: " + values['query'])
    print("[+] Country: " + values['country'])
    print("[+] ISP: " + values['isp'])
    print("[+] City: " + values['city'])
    print("[+] Region: " + values['region'])
    print("[+] TimeZone: " + values['timezone'])
elif opt == 2:
    exit
