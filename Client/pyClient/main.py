from world import World
from player import Player

import pygame

world = World()
player = Player((100,100))

world.player = player
world.main()
