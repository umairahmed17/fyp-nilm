from const import *
from square import Square
from piece import *
from move import Move

class Board:
    
    def __init__(self) -> None:
        self.squares: list[list[Square]] = []
        self._create()
        self._add_piece('white')
        self._add_piece('black')
        
    def calculate_moves(self, piece, row, col):
        # Calculate all possible moves
        if isinstance(piece, Pawn):
            pass
        
        if isinstance(piece, Knight):
            possible_moves = Knight.possible_moves(row=row, col=col)        
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                
                if Square.in_range(possible_move_col, possible_move_row):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_rival(piece.color):
                        # create squares for move
                        initial = Square(row=row, col=col)
                        final = Square(row=possible_move_row, col=possible_move_col) # we have to pass a piece
                        
                        # create new move
                        move = Move(initialSquare=initial, finalSquare=final)
                        
                        # append new valid move
                        piece.add_move(move)
        
        if isinstance(piece, Bishop):
            pass
        
        if isinstance(piece, Rook):
            pass
        
        if isinstance(piece, Queen):
            pass
        
        if isinstance(piece, King):
            pass
        pass
    
    def _create(self):
        self.squares = [[0] * 8 for col in range(COLS)]
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    
    def _add_piece(self, color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)
        
        #pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        #knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        #bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        
        #rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        
        #queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        #king
        self.squares[row_other][4] = Square(row_other, 4, King(color))
