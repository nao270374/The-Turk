from enum import ENum, auto

# management class of games win or lose
class GameState(Enum):
    DRAW = auto()
    ON = auto()
    OVER = auto()
    