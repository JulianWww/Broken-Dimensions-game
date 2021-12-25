from time import time
import config
from player import Player


class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pawns = {}
        self.players = []
        self.connections = []
        self.lastTime = time()

    def update(self):
        currentTime = time()
        dt = currentTime - self.lastTime
        for pawn in self.pawns.values():
            pawn.update(dt)

        self.lastTime = currentTime

    def mainloop(self):
        self.lastTime = time()
        while not self.isDone():
            self.update()

    def isDone(self):
        return False

    def addPawn(self, pawn):
        pawn.world = self
        self.pawns[id(pawn)] = pawn

        for connection in self.connections:
            connection.addPawn(pawn)

        startSendingData = getattr(pawn, "startSendingData", None)
        if not startSendingData is None:
            startSendingData()
            self.connections.append(pawn)
            pawn.putInWorld(self)

    def getPosData(self, playerID):
        data = [[]]
        for pawn in self.pawns.values():
            if (id(pawn) != playerID):
                data[0].append(id(pawn))
                data[0].append(float(pawn.pos[0]))
                data[0].append(float(pawn.pos[1]))
                data[0].append(float(pawn.vel[0]))
                data[0].append(float(pawn.vel[1]))
        return data
        
        
