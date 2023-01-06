import pygame
from const import *
from piece import Piece

class Dragger:
    
    def __init__(self) -> None:
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.dragging = False
     
    #blit methods
    
    def update_blit(self, surface) -> None:
        # making draggable piece bigger
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        
        #img
        img = pygame.image.load(texture)
        
        #rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)
        
        #blit
        surface.blit(img, self.piece.texture_rect)
    
    #mouse methods
    
    def update_mouse(self, pos: tuple(float, float)) -> None:
        self.mouseX, self.mouseY = pos # (xcor, ycor)
        
    def save_initial(self, pos) -> None:
        self.initial_row = pos[1] // SQUARE_SIZE
        self.initial_col = pos[0] // SQUARE_SIZE
        
    def drag_piece(self, piece: Piece) -> None:
        self.piece = piece
        self.dragging = True
        
    def undrag_piece(self) -> None:
        self.piece = None
        self.dragging = False