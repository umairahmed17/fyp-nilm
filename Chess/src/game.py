import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:
    
    def __init__(self) -> None:
        self.board = Board()
        self.dragger = Dragger()
    
    # Show methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (234, 235, 200) # light green
                else:
                    color = (119, 154, 88) # dark green
                
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                
                pygame.draw.rect(surface, color, rect)
                
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)
                        
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            
            for move in piece.moves:
                # create a color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # create a rect
                rect = (move.final.col * SQUARE_SIZE, move.final.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                # blit
                pygame.draw.rect(surface, color=color, rect=rect)