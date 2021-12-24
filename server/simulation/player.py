from pawn import Pawn

class Player(Pawn):
    PAWNTYPE = 1
    def __init__(self, *args):
        super(Player, self).__init__(*args)
