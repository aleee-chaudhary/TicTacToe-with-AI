import random
import math

class minmax_algo():
    def __init__(self, level=1):
        self.level = level

    def minmax(self, board, maximizing):
        case = self.evaluate_game(board)

        if case == 1:
            return {'pos': None, 'score': 1}

        if case == -1:
            return {'pos': None, 'score': -1}

        if board.is_full():
            return {'pos': None, 'score': 0}

        if maximizing:
            best = {'pos': None, 'score': -math.inf}

            for (row, col) in board.get_empty_sqrs():
                board.mark_square(row, col, 'O')
                sim_sc = self.minmax(board, False)
                board.squares[row][col] = ''  # Undo move   
                board.mark_squares -= 1
                sim_sc['pos'] = (row, col)
                if sim_sc['score'] > best['score']:
                    best = sim_sc

            return best

        else:
            best = {'pos': None, 'score': math.inf}

            for (row, col) in board.get_empty_sqrs():
                board.mark_square(row, col, 'X')
                sim_sc = self.minmax(board, True)
                board.squares[row][col] = ''  # Undo move
                board.mark_squares -= 1
                sim_sc['pos'] = (row, col)
                if sim_sc['score'] < best['score']:
                    best = sim_sc

            return best

    def evaluate_game(self, board):
        # Vertical check
        for col in range(3):
            if (board.squares[0][col] == board.squares[1][col] == board.squares[2][col]) and (board.squares[0][col] != ''):
                if board.squares[0][col] == 'O':
                    return 1
                elif board.squares[0][col] == 'X':
                    return -1

        # Horizontal check
        for row in range(3):
            if (board.squares[row][0] == board.squares[row][1] == board.squares[row][2]) and (board.squares[row][0] != ''):
                if board.squares[row][0] == 'O':
                    return 1
                elif board.squares[row][0] == 'X':
                    return -1

        # Descending diagonal check
        if (board.squares[0][0] == board.squares[1][1] == board.squares[2][2]) and (board.squares[0][0] != ''):
            if board.squares[0][0] == 'O':
                return 1
            elif board.squares[0][0] == 'X':
                return -1

        # Ascending diagonal check
        if (board.squares[2][0] == board.squares[1][1] == board.squares[0][2]) and (board.squares[2][0] != ''):
            if board.squares[2][0] == 'O':
                return 1
            elif board.squares[2][0] == 'X':
                return -1

        return 0