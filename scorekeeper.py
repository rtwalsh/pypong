import pygame

class Scorekeeper():

    LEFT_PLAYER = 0
    RIGHT_PLAYER = 1

    def __init__(self):
        self.scores = [ 0, 0 ]
        self.score_sound = pygame.mixer.Sound("./assets/sounds/mixkit-retro-game-notification-212.wav")

    def award_point(self, which_player):
        self.score_sound.play()
        self.scores[which_player] += 1
        print("Score:", self.scores)

    def get_score(self, which_player):
        return self.scores[which_player]
    
    def is_game_over(self):
        return self.scores[Scorekeeper.LEFT_PLAYER] == 9 or self.scores[Scorekeeper.RIGHT_PLAYER] == 9