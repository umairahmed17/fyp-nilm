from piece import Piece

class Square:
    
    def __init__(self, row:int, col:int, piece: Piece | None=None) -> None:
        self.row = row
        self.col = col
        self.piece = piece
        
    def has_piece(self) -> bool:
        return self.piece != None
    
    def has_rival_piece(self, color) -> bool:
        return self.has_piece() and self.piece.color != color

    def is_empty(self) -> bool:
        return not self.has_piece()
    
    def has_team_piece(self, color) -> bool:
        return self.has_piece() and self.piece.color == color
    
    def is_empty_or_rival(self, color) -> bool:
        return self.is_empty() or self.has_rival_piece(color)
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
            
        return True