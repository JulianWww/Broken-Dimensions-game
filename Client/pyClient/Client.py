import socket
import requests
import time
from threading import Thread
from pickle import loads, dumps
from pawnIDs import getPawnType


class Client:
    def __init__(self, player, world):
        address = requests.get("http://wandhoven.ddns.net/code/BrokenDimentions/serverip").content.decode("utf-8")
        dot = address.index(":")
        self.messageID = 0
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((address[:dot], int(address[dot+1:])))

        player.id = int.from_bytes(self.sock.recv(8), "little")
        self.world = world

        self.recvThread = Thread(target=self.mainloop, daemon=False)
        self.recvThread.start()

    def sendData(self, data):
        data = dumps(data)
        dataSize = len(data)
        self.sock.send(int.to_bytes(dataSize, 4, "little"))
        self.sock.send(data)

    def recvData(self):
        size = int.from_bytes(self.sock.recv(4), "little")
        data = loads(self.sock.recv(size))
        return data

    def move(self, data):
        unknown_pawns = []
        for ID, x, y, dx, dy in zip(data[::5], data[1::5], data[2::5], data[3::5], data[4::5]):
            try:
                actor = self.world.pawns[ID]
                actor.pos = (x,y)
                actor.velocity = (dx, dy)
            except KeyError:
                unknown_pawns.append(ID)
        return unknown_pawns

    def getPlayerData(self):
        data = []

        data.append(self.world.player.getData())
        return data

    def actOnQuery(self, data):
        for dataPointId, dataPoint in data:
            if dataPointId == 0:
                self.addPawns(dataPoint)

    def addPawns(self, data):
        print(data)
        for ID, TYPE in zip(data[::2], data[1::2]):
            p = getPawnType(TYPE)((0,0), ID)
            self.world.addPawn(p)

    def mainloop(self):
        while not self.world.isDone():
            data = self.recvData()
            sendData = self.getPlayerData()
            self.actOnQuery(data[1])
            unknown_pawns = self.move(data[0])
            if len(unknown_pawns):
                sendData.append((0, unknown_pawns))
            self.sendData(sendData)

if __name__ == "__main__":
    c = Client(None)
    print(c.recvData())
