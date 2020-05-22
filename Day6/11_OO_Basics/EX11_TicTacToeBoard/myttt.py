class TicTacToeBoard:
    def __init__(self):
        location = int(0)
        token = str(None)
        pass

    def make_a_move(self,location,token):
        self.location = location
        self.token = token
        print('Setting',token,'to',location)

    def get_location(self,location):
        t = self.location
        return t

    def check_game_status(self):
        print('Still playing!')

my_game = TicTacToeBoard()
my_game.make_a_move(5,'x')
print(my_game.get_location(0))
my_game.check_game_status()