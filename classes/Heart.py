import random

import pygame

from constants import *
from helpers import screen


class Heart:
    def __init__(self):
        self.size = 20
        self.image = pygame.transform.scale(pygame.image.load("Images/heart.png"), (self.size, self.size))
        self.location = [random.randint(50, WINDOW_WIDTH - 50), WINDOW_HEIGHT - self.size]
        self.speed = 10

    def move(self):
        screen.blit(self.image, self.location)
        self.location[1] -= self.speed

    def get_y(self):
        return self.location[1]

    def get_height(self):
        return self.size
