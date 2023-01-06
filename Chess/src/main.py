import pygame
import sys

from const import *
from game import Game

class Main:
    
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption("Chess")
        self.game = Game()

    def mainLoop(self):
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board
        

            
        while True:
            game.show_bg(screen)
            game.show_moves(surface=screen)
            game.show_pieces(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)
            
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    
                    clicked_row = dragger.mouseY // SQUARE_SIZE
                    clicked_col = dragger.mouseX // SQUARE_SIZE
                    
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calculate_moves(piece=piece, row=clicked_row, col=clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        
                        # show
                        game.show_bg(surface=screen)
                        game.show_moves(surface=screen)
                        game.show_pieces(surface=screen)
                        
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(surface=screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()
                
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
    
    
main = Main()

main.mainLoop()