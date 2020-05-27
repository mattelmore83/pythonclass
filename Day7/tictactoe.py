#
# Code planning and organization exercise
#

# Loop

# Ask player X for a move
# Put an X on the board at that spot
# Check board status

# Ask player O for a move
# Put an O on the board at that spot
# Check board status

# --------------------------------------------------------------------------------------------

# token is used to differentiate between the two players
# location is a single integer 0 top left and 8 bottom right to indicate the spot on the board

def print_board():
    print(
        board[0] + '|' + board[1] + '|' + board[2] + '\n' +
        '-+-+-\n' +
        board[3] + '|' + board[4] + '|' + board[5] + '\n' +
        '-+-+-\n' +
        board[6] + '|' + board[7] + '|' + board[8] + '\n'
    )


def get_move(token):
    print_board()
    print('Your move player', token)
    loc = int(input('Where do you want to go (0-8):'))
    return loc


def set_token(token, location):
    board[location] = token


def get_token(location):
    r = board[location]
    return r


def _check_token(token):
    # check for row wins
    if board[0] == token and board[1] == token and board[2] == token:
        return True  # top row
    if board[3] == token and board[4] == token and board[5] == token:
        return True  # middle row
    if board[6] == token and board[7] == token and board[8] == token:
        return True  # bottom row

    # check for column wins
    if board[0] == token and board[3] == token and board[6] == token:
        return True  # left column
    if board[1] == token and board[4] == token and board[7] == token:
        return True  # middle column
    if board[2] == token and board[5] == token and board[8] == token:
        return True  # right column

    # check for diagonal wins
    if board[0] == token and board[4] == token and board[8] == token:
        return True  # upper left to lower right
    if board[2] == token and board[4] == token and board[6] == token:
        return True  # upper right to lower left


def get_status():
    # Four possibilities: 'playing', 'tie', 'x wins', 'o wins'

    # check for winner
    if _check_token('X'):
        return 'X won'
    if _check_token('O'):
        return 'O won'

    # check for a tie
    if ' ' in board:
        return 'Still playing'
    else:
        return 'Tie'


# build empty board
# board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = [' '] * 9  # create an array of 9 empty strings

while True:
    # main logic
    loc = get_move('X')
    set_token('X', loc)
    s = get_status()
    if s != 'Still playing':
        break

    loc = get_move('O')
    set_token('O', loc)
    s = get_status()
    if s != 'Still playing':
        break

# end of game screen
print_board()
print(s)
