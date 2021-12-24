from player import BasePlayer

_pawnTypes = {
    BasePlayer.PAWNTYPE: BasePlayer
}

def getPawnType(typeID):
    return _pawnTypes[typeID]
