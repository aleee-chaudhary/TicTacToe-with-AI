import pygame
import sys
from board import board
from minmax_algo import minmax_algo
from constants import *

class game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe by AI')
        self.board = board()
        self.minmax_algo = minmax_algo()
        self.player = 'X'  # Human player starts
        self.running = True
        self.gameOver = False

    def mainloop(self):
        while self.running:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.gameOver and self.player == 'X':  # Human player's turn
                    pos = event.pos
                    row = pos[1] // SQSIZE
                    col = pos[0] // SQSIZE
                    
                    if self.board.is_empty_squares(row, col):
                        self.board.mark_square(row, col, self.player)
                        if self.board.check_winner(self.player):
                            self.gameOver = True
                            self.running = False
                        elif self.board.is_full():
                            self.gameOver = True  # Game over due to a draw
                            self.running =False
                        else:
                            self.player = 'O'  # Switch to AI player

    def update(self):
        if not self.gameOver and self.player == 'O':  # AI player's turn
            move = self.minmax_algo.minmax(self.board, True)
            if move['pos'] is not None:
                row, col = move['pos']
                self.board.mark_square(row, col, self.player)

            if self.board.check_winner(self.player):
                self.gameOver = True
                self.running = False
            elif self.board.is_full():
                self.gameOver = True  # Game over due to a draw
                self.running = False
            else:
                self.player = 'X'  # Switch back to the human player

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.board.draw(self.screen)
        pygame.display.update()

if __name__ == '__main__':
    game = game()
    game.mainloop()