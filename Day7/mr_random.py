from player import Player
import random


class MrRandom(Player):

    def get_move(self, board):
        #print(board)
        possible_moves = []
        for i in range(9):
            if board.get_token(i) == ' ':
                possible_moves.append(i)
        return random.choice(possible_moves)
