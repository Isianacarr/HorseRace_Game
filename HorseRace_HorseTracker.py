import random
import sys
import pygame
from pygame.locals import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Horse(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super().__init__()
        self.image = pygame.image.load(image)
        #self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = (width,height)
        self.score = 0


    def draw(self,surface):
        surface.blit(self.image, self.rect)
        return self

    def add_to_score(self):
        self.score += 1

    def sub_from_score(self):
        self.score -=1

    def move_horse(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

























