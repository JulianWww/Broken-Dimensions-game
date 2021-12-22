import config



class Pawn():
    def __init__(self, pos):
        self.pos = pos
        self.velocity = (0, 0)

    def update(self, dt):
        x, y = self.pos
        dx, dy = self.velocity
        x, y = x + dx, y + dy

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

        
