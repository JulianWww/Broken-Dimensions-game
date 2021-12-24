import socket
import requests

class Client:
    def __init__(self):
        address = requests.get("http://wandhoven.ddns.net/code/BrokenDimentions/serverip").content.decode("utf-8")
        dot = address.index(":")
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address[:dot], int(address[dot+1:])))

        self.id = int.from_bytes(self.sock.recv(4), "little")
        print(self.id)

        self.sendAction(10, None)

    def sendAction(self, actionId, data):
        self.sock.send(int.to_bytes(actionId, 1, "little"))


Client()
