import pygame

from classes.Post import Post
from constants import *
from helpers import screen, from_text_to_array, center_text


class TextPost(Post):
    def __init__(self, name, loc, desc, text, text_color, background_color):
        super().__init__(name, loc, desc)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color

    # Displays the background onto the post square and then displays the text centered.
    def display(self):
        super().display()
        background = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, background)

        text_array = from_text_to_array(self.text)
        for i in range(len(text_array)):
            line_loc = center_text(len(text_array), text_array[i], i)
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(self.text, True, self.text_color)
            screen.blit(text, line_loc)
