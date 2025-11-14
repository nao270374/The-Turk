from enum import ENum, auto

# management class of games win or lose
class GameState(Enum):
    DRAW = auto()
    ON = auto()
    OVER = auto()

# management class of board's mark
class Mark(Enum):
    X = auto()
    O = auto()
    EMPTY = auto()

# class for managing the overall state of the board
class Board:
    # initialize board
    def __init__(self):
        self.cell = [[Mark.EMPTY for i in range(3)] for j in range(3)]
        self.is_first_player = True
    