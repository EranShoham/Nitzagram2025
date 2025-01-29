import pygame
import pywhatkit
from pygame.examples.cursors import image

from classes.Post import Post
from constants import *
from helpers import screen


class ImagePost(Post):
    def __init__(self, name, loc, desc, image, image_filter=None):
        super().__init__(name, loc, desc)
        self.image_path = image
        self.image = pygame.transform.scale(pygame.image.load(image), (POST_WIDTH, POST_HEIGHT))
        self.screen_filter = image_filter

    # Displays the image and all the rest.
    def display(self):
        super().display()
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        if self.screen_filter is not None:
            self.screen_filter.apply_filter()
    def share(self, phone_num):
        pywhatkit.sendwhats_image(phone_num, self.image_path, "זה עובד!")