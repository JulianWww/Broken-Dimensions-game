from pawn import Pawn
import pygame, config


class BasePlayer(Pawn):
    PAWNTYPE = 1
    def __init__(self, *args):
        super(BasePlayer, self).__init__(*args)

        self.sprite = pygame.image.load("characters/player.png")

    def render(self, win):
        win.blit(pygame.transform.scale(self.sprite, (300, 300)), (self.pos[0], self.pos[1]))

class Player(BasePlayer):
    def __init__(self, *args):
        super(Player, self).__init__(*args)

        self.jumps = 0
        self.jumped = False

    def update(self, dt):
        super(Player, self).update(dt)

        dx, dy = self.velocity
        keys = pygame.key.get_pressed()

        if (self.pos[1] == config.floorLevel):
            self.jumps = 0

        if keys[pygame.K_SPACE]:
            if (self.jumps < 2 and not self.jumped):
                self.jumps += 1
                dy += config.playerJumpVelocity
                self.jumped = True
        else:
            self.jumped = False

        if keys[pygame.K_a]:
            dx -= config.playerHorizontalAcceleration
        if keys[pygame.K_d]:
            dx += config.playerHorizontalAcceleration

        self.velocity = dx, dy

    def getData(self):
        return [self.pos[0], self.pos[1], self.velocity[0], self.velocity[1]]

    
