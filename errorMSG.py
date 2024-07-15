# coded By 0xdyBlack

def using():
    msg = """
    -u , --url     : inter URL and in file inter DYBLACK404 Like < https://exampel/getImage?file=DYBLACK404 >
    -m , --mutod   : MUTOD : http-post , http-get , ftp , ssh
    -f , --file    : get me name file Ex = -f "/etc/passwd" 
    -r , --respons : get me name in out put Ex = "root"
    -l , --loop     : inter numper of ../ 
    -a , --add     : if you need inter null bute like "%00" or "0x00" 
    """
    baner = """
    _______             .___      __________.__                 __      _____  _______      _____  
    \   _  \ ___  ___ __| _/__.__.\______   \  | _____    ____ |  | __ /  |  | \   _  \    /  |  | 
    /  /_\  \\  \/  // __ <   |  | |    |  _/  | \__  \ _/ ___\|  |/ //   |  |_/  /_\  \  /   |  |_
    \  \_/   \>    </ /_/ |\___  | |    |   \  |__/ __ \\  \___|    </    ^   /\  \_/   \/    ^   /
     \_____  /__/\_ \____ |/ ____| |______  /____(____  /\___  >__|_ \____   |  \_____  /\____   | 
           \/      \/    \/\/             \/          \/     \/     \/    |__|        \/      |__|                             
    """
    return msg, baner

def errorRunLbrary():
    msg = "Pls This File Is Labrary Not Script Pls Run dyBlack Tool !"
    return msg

def errorInUsing():
    msg = "Your Input Is Not Vulad :( "
    return msg

def url_is_not_fond():
    msg = "URL Not Found :( "
    return msg

if __name__  == "__main__" :
    msg = errorRunLbrary()
    print(msg)