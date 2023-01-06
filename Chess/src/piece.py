import os
from move import Move

class Piece:
    def __init__(self, name, color, value, texture=None , texture_rect= None) -> None:
        self.name = name
        self.color = color
        
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves: list[Move] = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size=80) -> None:
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )
        
    def add_move(self, move: Move) -> None:
        self.moves.append(move)
    
class Pawn(Piece):
    def __init__(self, color) -> None:
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1.0)
        
class Knight(Piece):
    def __init__(self, color) -> None:
        super().__init__('knight', color, 3.0)
        
    @staticmethod
    def possible_moves(row, col) -> list[tuple[int, int]]:
        # 8 possible moves
        return [
            (row - 2, col + 1),
            (row - 2, col - 1),
            (row - 1, col + 2),
            (row - 1, col - 2),
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col + 2),
            (row + 1, col - 2),
        ]
            
class Bishop(Piece):
    def __init__(self, color) -> None:
        super().__init__('bishop', color, 3.001)
        
        
class Rook(Piece):
    def __init__(self, color) -> None:
        super().__init__('rook', color, 5.0)
        
class Queen(Piece):
    def __init__(self, color) -> None:
        super().__init__('queen', color, 9.0)
        
class King(Piece):
    def __init__(self, color) -> None:
        super().__init__('king', color, 10000.0)