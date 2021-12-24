import pygame
from time import time
import config
from Client import Client
from player import Player

class Timer():
    def __init__(self):
        self.reset()
        
    def reset(self):
        self._time = time()

    def dt(self):
        newTime = time()
        dt = newTime - self._time
        self._time = newTime
        return dt


class World():
    WIDTH, HEIGHT = config.worldSize
    TITLE = "Broken Dimensions"
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        clock = pygame.time.Clock()

        player = Player((100,100), None)
        self.player = player
        self.pawns = {}
        
        self.client = Client(self.player, self)
        self.addPawn(self.player)
        self.timer = Timer()

    def isDone(self):
        return False

    def addPawn(self, pawn):
        self.pawns[pawn.id] = pawn

    def update(self, dt):
        self.handleEvents()

        for pawn in self.pawns.values():
            pawn.update(dt)

    def render(self):
        self.win.fill((12, 24, 36))
        for pawn in self.pawns.values():
            pawn.render(self.win)

        pygame.display.flip()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def main(self):
        self.timer.reset()
        while True:
            dt = self.timer.dt()
            self.update(dt)
            self.render()
        


if __name__ == "__main__":
    world = World()
