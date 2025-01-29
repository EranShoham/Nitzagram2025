import pygame
from constants import *
from helpers import screen


class Filter:
    def __init__(self, color , alpha):
        self.color = color
        self.alpha = alpha

    def apply_filter(self):
        filter_rect = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        filter_rect.fill(self.color)
        filter_rect.set_alpha(self.alpha)
        screen.blit(filter_rect, (POST_X_POS, POST_Y_POS))