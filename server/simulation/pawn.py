import numpy as np
import config


class Pawn:
    def __init__(self, pos, vel):
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.id = id(self)

    def update(self, dt):
        self.move(dt)
        self.contrainPosition(dt)
        self.velocityDecay(dt)

    def move(self, dt):
        self.pos += self.vel * dt

    def gravityAcceleration(self, dt):
        self.vel[1] += config.gravity * dt

    def velocityDecay(self, dt):
        if dt != 0:
            self.vel[0] *= config.playerHorizontalVelocityDecay ** (1/dt)

    def contrainPosition(self, dt):
        # constrin due to flor
        if self.pos[1] > config.floorLevel:
            self.pos[1] = config.floorLevel
            self.vel[1] = 0

        else: self.gravityAcceleration(dt)

        #border wall constraints
        if self.pos[0] < config.pawnHorizontalConstaint[0]:
            self.pos[0] = config.pawnHorizontalConstaint[0]
            self.vel[0] *= -1

        if self.pos[1] > config.pawnHorizontalConstaint[1]:
            self.pos[1] = config.pawnHorizontalConstaint[0]
            self.vol[1] *= -1
