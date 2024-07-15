# coded by 0xdyblack404

from errorMSG import errorRunLbrary
import requests

def send_http_req(url, res):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.3"}
    req = requests.get(url, headers=headers)
    if res.encode() in req.content:
        return 1
    else :
        return -1
