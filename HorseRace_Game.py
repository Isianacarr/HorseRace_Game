import HorseRace_HorseTracker
#import HorseRace_Player
import random
import sys
import pygame
from pygame.locals import *




pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

DISPLAYSURF =pygame.display.set_mode((600,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Horse Race")

class Game():
    def __init__(self):
        self.gui = pygame.init()
        self.round = 0



    def create_Player(self):
        player_name = input("Please Enter your name.")
        player_cash = input("How much cash would you like to add to you books?")
        #player = HorseRace_Player.Player(player_name,player_cash)

    def create_Horse(self, image, width, height):

        horse = HorseRace_HorseTracker.Horse(image,width,height)
        horse.draw(self.gui)

        return horse













moving_right = False
moving_left = False

game = Game(DISPLAYSURF)
horse1 = game.create_Horse("Horse Photos/Black Horse.jpg", 100 ,550)
horse2 = game.create_Horse("Horse Photos/Grey Horse.jpg", 250, 550)
horse3 = game.create_Horse("Horse Photos/Light Brown Horse.jpg", 400, 550)
horse4 = game.create_Horse("Horse Photos/dark brown horse.jpg", 550, 550)

moving = False
while True:

    if moving == True:
        horse1.move_horse()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            moving = True
        if event.type == KEYUP:
            moving = False
    horse1.move_horse()








    pygame.display.update()
    FramePerSec.tick(FPS)