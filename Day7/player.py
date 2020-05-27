
class Player:

    def __init__(self,token):
        self._token = token

    def get_move(self,board):
        # TODO: error checking
        print(board)
        print('Your move player', self._token)
        loc = int(input('Where do you want to go (0-8):'))
        return loc