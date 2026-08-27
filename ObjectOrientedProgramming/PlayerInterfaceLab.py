from abc import ABC, abstractmethod
import random
class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    
    def make_move(self):
        x,y = random.choice(self.moves)
        x2,y2 = self.position
        self.position = (x+x2,y+y2)
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        pass
    
class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1),(1,0),(-1,0),(0,-1)]
    
    def level_up(self):
        self.moves.append((1,1))
        self.moves.append((-1,1))
        self.moves.append((1,-1))
        self.moves.append((-1,-1))
