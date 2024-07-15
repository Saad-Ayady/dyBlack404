# coded by 0xdyBlack404

import urllib.parse
from errorMSG import errorRunLbrary

def encode_to_url(string):
    new_data = ""
    start = 0
    while start < len(string):
        if string[start] == ".":
            new_data += "%2e"
        elif string[start] == "\\" :
            new_data += urllib.parse.quote_plus("\\")
        elif string[start] == "/" :
            new_data += urllib.parse.quote_plus("/")
        else :
            new_data = new_data + string[start]
        start += 1
    return new_data

def encode_to_16bate(string):
    new_data = ""
    start = 0
    while start < len(string) :
        if string[start] == ".":
            new_data += "%u002e"
        elif string[start] == "/":
            new_data += "%u2215"
        elif string[start] == "\\" :
            new_data += "%u2216"
        else :
            new_data += string[start]
        start += 1
    return new_data

def doble_encode_to_url(string):
    new_str = ""
    furst_enced = encode_to_url(string)
    new_str = furst_enced.replace("%5C", "%255C")
    new_str = furst_enced.replace("%2F", "%252F")
    new_str = furst_enced,replace("%2e", "%252e")
    return new_str

def encode_to_url_furst(string):
    new_data = ""
    start = 0
    while start < len(string):
        if string[start] == "\\" :
            new_data += urllib.parse.quote_plus("\\")
        elif string[start] == "/" :
            new_data += urllib.parse.quote_plus("/")
        else :
            new_data = new_data + string[start]
        start += 1
    return new_data

def doble_encode_to_url_furst(string):
    new_str = ""
    furst_enced = encode_to_url(string)
    new_str = furst_enced.replace("%5C", "%255C")
    new_str = furst_enced.replace("%2F", "%252F")
    return new_str


def encode_UTF8_unicode_furst(string):
    new_data = ""
    start = 0
    while start < len(string) :
        if string[start] == ".":
            new_data += "%c0%2e"
        elif string[start] == "/":
            new_data += "%c0%af"
        elif string[start] == "\\" :
            new_data += "%c0%5c"
        else :
            new_data += string[start]
        start += 1
    return new_data

def encode_UTF8_unicode_sucend(string):
    new_data = ""
    start = 0
    while start < len(string) :
        if string[start] == ".":
            new_data += "%e0%40%ae"
        elif string[start] == "/":
            new_data += "%e0%80%af"
        elif string[start] == "\\" :
            new_data += "%c0%80%5c"
        else :
            new_data += string[start]
        start += 1
    return new_data

def encode_UTF8_unicode_trea(string):
    new_data = ""
    start = 0
    while start < len(string) :
        if string[start] == ".":
            new_data += "%c0ae"
        elif string[start] == "/":
            new_data += "%c0%2f"
        elif string[start] == "\\" :
            new_data += "%c0%80%5c"
        else :
            new_data += string[start]
        start += 1
    return new_data


if __name__  == "__main__" :
    msg = errorRunLbrary()
    print(msg)