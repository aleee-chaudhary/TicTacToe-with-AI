import pygame
from constants import *

class board():
    def __init__(self):
        self.squares = [['' for _ in range(COLS)] for _ in range(ROWS)]
        self.empty_squares = []
        self.mark_squares = 0

    def draw(self,screen):
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)

        # Drawing X's and O's
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col] == 'X':
                    # Draw X
                    start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                    end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                    pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

                    start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                    end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                    pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
                
                elif self.squares[row][col] == 'O':
                    # Draw O
                    center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)


    def mark_square(self,row,col,player):
        self.squares[row][col] = player
        self.mark_squares +=1


    def is_empty_squares(self,row,col):
        return self.squares[row][col] == ''

    def get_empty_sqrs(self):
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_empty_squares(row,col):
                    empty_squares.append((row,col))

        return empty_squares


    def is_full(self):
        return self.mark_squares == 9

    def is_empty(self):
        return self.mark_squares == 0

    def check_winner(self, player):
        # Vertical check
        for col in range(COLS):
            if self.squares[0][col] == player and self.squares[1][col] == player and self.squares[2][col] == player:
                return True

        # Horizontal check
        for row in range(ROWS):
            if self.squares[row][0] == player and self.squares[row][1] == player and self.squares[row][2] == player:
                return True

        # Descending diagonal check
        if self.squares[0][0] == player and self.squares[1][1] == player and self.squares[2][2] == player:
            return True

        # Ascending diagonal check
        if self.squares[2][0] == player and self.squares[1][1] == player and self.squares[0][2] == player:
            return True

        return False
