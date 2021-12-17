import socket
import requests

class Client:
    def __init__(self):
        address = requests.get("http://wandhoven.ddns.net/code/BrokenDimentions/serverip").content.decode("utf-8")
        dot = address.index(":")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address[:dot], int(address[dot+1:])))
        print(sock)


Client()
