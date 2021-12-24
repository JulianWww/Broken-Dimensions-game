from simulation.world import World
from simulation.pawn import Pawn
from connection import Connection


world = World()

player = Connection([100.0,100.0], [0.0,0.0])
world.addPawn(player)

player2 = Connection([100.0,100.0], [0.0,0.0])
world.addPawn(player2)

world.mainloop()
