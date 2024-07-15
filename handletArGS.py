# coded by 0xdyBlack404

from sys import argv
from errorMSG import errorRunLbrary

def send_arg(all_argse) :
    url      = ""
    moted    = "http-get"
    file     = "/etc/passwd"
    respo    = "root"
    loop     = 13
    nullByte = "NULL"
     
    if "-u" in all_argse or "--url" in all_argse:
        if "-u" in all_argse:
            url = all_argse[all_argse.index("-u") + 1]
        elif "--url" in all_argse:
            url = all_argse[all_argse.index("--url") + 1]
            
    if "-m" in all_argse or "--mutod" in all_argse :
        if "-m" in all_argse:
            moted = all_argse[all_argse.index("-m") + 1]
        elif "--mutod" in all_argse :
            moted = all_argse[all_argse.index("--mutod") + 1]
            
    if "-f" in all_argse or "--file" in all_argse :
        if "-f" in all_argse:
            file = all_argse[all_argse.index("-f") + 1]
        elif "--file" in all_argse :
            file = all_argse[all_argse.index("--file") + 1]
    
    if "-r" in all_argse or "--respons" in all_argse :
        if "-r" in all_argse:
            respo = all_argse[all_argse.index("-r") + 1]
        elif "--respons" in all_argse :
            respo = all_argse[all_argse.index("--respons") + 1]
    
    if "-l" in all_argse or "--loop" in all_argse :
        if "-l" in all_argse:
            loop = all_argse[all_argse.index("-l") + 1]
        elif "--loop" in all_argse :
            loop = all_argse[all_argse.index("--loop") + 1]
    
    if "-a" in all_argse or "--add" in all_argse :
        if "-a" in all_argse:
            nullByte = all_argse[all_argse.index("-a") + 1]
        elif "--add" in all_argse :
            nullByte = all_argse[all_argse.index("--add") + 1]
    
    if url != "" :
        return url, moted, file, respo, int(loop), nullByte
    else:
        return -1

if __name__ == "__main__" :
    print(errorRunLbrary())