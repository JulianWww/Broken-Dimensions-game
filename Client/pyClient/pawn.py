import config



class Pawn():
    def __init__(self, pos, ID):
        self.pos = pos
        self.velocity = (0, 0)
        self.id = ID

    def velocityDecay(self, dt):
        if (self.pos[1] >= config.floorLevel):
            dx, dy = self.velocity
            dx *= config.playerHorizontalVelocityDecay ** dt
            self.velocity = dx, dy

    def update(self, dt):
        x, y = self.pos
        dx, dy = self.velocity
        x, y = x + dx*dt, y + dy*dt

        if y > config.floorLevel:
            y = config.floorLevel
            dy = 0
        else:
            dy += config.gravity * dt

        if x < config.pawnHorizontalConstaint[0]:
            x = config.pawnHorizontalConstaint[0]
            dx *= -1

        if x > config.pawnHorizontalConstaint[1]:
            x = config.pawnHorizontalConstaint[1]
            dx *= -1

        
        self.velocity = dx, dy
        self.pos = x, y

        self.velocityDecay(dt)

        
