import HorseRace_HorseTracker
#import HorseRace_Player
import random
import sys
import pygame
from pygame.locals import *
import HorseRace_Game

class Reff():
    def __init__(self):
        pass

    def decide_who_moves(self):
        return random.randint(1,4)

    def game_in_progress(self):
        """Checks to see if any horses have a winning score. If so, then returns false.

        """
        if self.round < self.race_length:
            return True
        else:
            return False

    def winner(self):
        if self.game_in_progress() == False:
            return

