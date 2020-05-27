
class Board:

    def __init__(self):
        self._board = [' '] * 9  # create an array of 9 empty strings

    def __str__(self):
        ret = (
            self._board[0] + '|' + self._board[1] + '|' + self._board[2] + '\n' +
            '-+-+-\n' +
            self._board[3] + '|' + self._board[4] + '|' + self._board[5] + '\n' +
            '-+-+-\n' +
            self._board[6] + '|' + self._board[7] + '|' + self._board[8] + '\n'
        )
        return ret

    def set_token(self,token,location):
        self._board[location] = token

    def get_token(self,location):
        return self._board[location]

    def _check_token(self,token):
        # check for row wins
        if self._board[0] == token and self._board[1] == token and self._board[2] == token:
            return True  # top row
        if self._board[3] == token and self._board[4] == token and self._board[5] == token:
            return True  # middle row
        if self._board[6] == token and self._board[7] == token and self._board[8] == token:
            return True  # bottom row

        # check for column wins
        if self._board[0] == token and self._board[3] == token and self._board[6] == token:
            return True  # left column
        if self._board[1] == token and self._board[4] == token and self._board[7] == token:
            return True  # middle column
        if self._board[2] == token and self._board[5] == token and self._board[8] == token:
            return True  # right column

        # check for diagonal wins
        if self._board[0] == token and self._board[4] == token and self._board[8] == token:
            return True  # upper left to lower right
        if self._board[2] == token and self._board[4] == token and self._board[6] == token:
            return True  # upper right to lower left

    def get_status(self):
        # Four possibilities: 'playing', 'tie', 'x wins', 'o wins'

        # check for winner
        if self._check_token('X'):
            return 'X won'
        if self._check_token('O'):
            return 'O won'

        # check for a tie
        if ' ' in self._board:
            return 'Still playing'
        else:
            return 'Tie'
