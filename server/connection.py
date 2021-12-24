import socket
from time import time, sleep
from threading import Thread
from simulation.player import Player
from pickle import dumps, loads
from select import select
import config

class Acceptor:
    def __init__(self):
        HOST = ""
        PORT = 25600
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(5)

    def accept(self):
        print("waiting for connection")
        sock, other = self.sock.accept()
        print("gotConnection from:", other)
        return sock

acceptor = Acceptor()


class Connection(Player):
    def __init__(self, *args):
        super(Connection, self).__init__(*args)
        self.sock = acceptor.accept()
        self.sendId()

    def sendId(self):
        self.sock.send(int.to_bytes(self.id, 8, "little"))

    def sendData(self, data):
        data = dumps(data)
        dataSize = len(data)
        self.sock.send(int.to_bytes(dataSize, 4, "little"))
        self.sock.send(data)

    def startSendingData(self):
        self.updateThread = Thread(target=self.sendDataLoop, daemon=False)
        self.updateThread.start()

    def getData(self):
        toRead, _, _ = select([self.sock], [], [])
        back = []
        for sock in toRead:
            size = int.from_bytes(sock.recv(4), "little")
            data = loads(sock.recv(size))
            self.updatePositionAndVelocity(data[0])

            for furtherData in data[1:]:
                if furtherData[0] == 0:
                    back.append((0,self.getPawnTypeIds(furtherData[1])))
        return back

    def getPawnTypeIds(self, ids):
        returns = []
        for ID in ids:
            pawn = self.world.pawns[ID]

            returns.append(ID)
            returns.append(pawn.PAWNTYPE)
        return returns          
        

    def updatePositionAndVelocity(self, data):
            self.pos[0] = data[0]
            self.pos[1] = data[1]
            self.vel[0] = data[0]
            self.vel[1] = data[1]

    def sendDataLoop(self):
        queryReturns = []
        while not self.world.isDone():
            data = self.world.getPosData(id(self))
            data.append(queryReturns)
            self.sendData(data)
            queryReturns = self.getData()
            sleep(config.updateIntervall)
