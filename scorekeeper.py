class Scorekeeper():

    LEFT_PLAYER = 0
    RIGHT_PLAYER = 1

    def __init__(self):
        self.scores = [ 0, 0 ]

    def award_point(self, which_player):
        self.scores[which_player] += 1
        print("Score:", self.scores)

    def get_score(self, which_player):
        return self.scores[which_player]
    
    def is_game_over(self):
        return self.scores[Scorekeeper.LEFT_PLAYER] == 9 or self.scores[Scorekeeper.RIGHT_PLAYER] == 9