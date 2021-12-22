import pygame, sys

# Constants
WIDTH, HEIGHT = 1800, 1000
TITLE = "Broken Dimensions"

# pygame initialization
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

playerIMG = pygame.image.load("characters/player.png")


# Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.char = win.blit(pygame.transform.scale(playerIMG, (300, 300)), (self.x, self.y))
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        self.jumpspeed = 8
        self.touchingground = True
        self.jumped = False

    def draw(self, win):
        # pygame.draw.rect(win, self.color, self.rect)
        win.blit(pygame.transform.scale(playerIMG, (300, 300)), (self.x, self.y))

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.jumpspeed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.char = pygame.Rect(int(self.x), int(self.y), 32, 32)
        # self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


# Player Initialization
player = Player(WIDTH / 2, HEIGHT / 2)

# Main Loop
while True:
    print(str(player.y))
    if player.y >= 700:
        player.touchingground = True
        player.jumped = False
    else:
        player.touchingground = False
        player.jumped = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.right_pressed = True
            if event.key == pygame.K_SPACE and player.touchingground and player.jumped == False:
                player.up_pressed = True
                player.jumped = True
            if event.key == pygame.K_s:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.right_pressed = False
            if event.key == pygame.K_SPACE or player.jumped:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.down_pressed = False

    # Draw
    win.fill((12, 24, 36))
    player.draw(win)

    # update
    player.update()
    pygame.display.flip()

    clock.tick(120)
