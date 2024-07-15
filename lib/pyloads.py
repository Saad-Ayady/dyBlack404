# coded by 0xdyBlack404
 
from errorMSG import errorRunLbrary

def normalpy(loop, pyload) :
    nwe_data = ""
    start = 0 
    while start <= loop :
        nwe_data += pyload 
        start += 1
    return nwe_data

if __name__  == "__main__" :
    msg = errorRunLbrary()
    print(msg)