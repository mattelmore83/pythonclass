
from board import Board
from player import Player
from mr_random import MrRandom

# BIG BANG or start of program
# Objects come into existence

board = Board()
player1 = Player('X')
#player1 = MrRandom('X')
#player2 = Player('O')
player2 = MrRandom('O')

while True:
    m = player1.get_move(board)
    board.set_token('X',m)
    s = board.get_status()
    if s != 'Still playing':
        break

    n = player2.get_move(board)
    board.set_token('O',n)
    s = board.get_status()
    if s != 'Still playing':
        break

# end of game screen
print(board)
print(s)
