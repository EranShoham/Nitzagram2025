import pygame
import pywhatkit

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
            font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = font.render(text_array[i], True, self.text_color)
            line_loc = center_text(len(text_array), text, i)
            screen.blit(text, line_loc)
    def share(self, phone_num):
        pywhatkit.sendwhatmsg_instantly(phone_num, "זה עובד!")
