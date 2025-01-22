import pygame

from constants import *
from helpers import screen
from classes.Post import Post

class ImagePost(Post):
    def __init__(self, name, loc, desc, image):
        super().__init__(name, loc, desc)
        self.image = pygame.transform.scale(pygame.image.load(image), (POST_WIDTH, POST_HEIGHT))

    # Displays the image and all the rest.
    def display(self):
        super().display()
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))