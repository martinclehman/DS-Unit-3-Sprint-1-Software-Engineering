'''
DSPT1-Lecture 312-OOP and Code Style
'''

class Game:
    """General representation of a game"""
    def __init__(self):
        self.round = 3
        self.player1 = 'Tina'
        self.player2 = 'Raul'

    def print_players(self):
        """Print the players of the game"""
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_rounds(self):
        """Incrementing the number of rounds by 1"""
        self.round += 1

    def winner(self):
        return(self.player1 if random() > 0.5 else self.player2)

class TicTacToe(Game):
    def __init__(self, max_rounds=5, player1='Joe', player2='Bill'):
        super().__init__(player1, player2)

    def print_players(self):
        """Print the players of the game"""
        print('{} is playing Tic-Tac-Toe with {}'.format(self.player1,
                                                         self.player2))
        
