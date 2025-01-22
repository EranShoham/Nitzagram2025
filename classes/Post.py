import pygame

from constants import *
from helpers import screen
import Comment


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, name, loc, desc):
        self.username = name
        self.location = loc
        self.description = desc
        self.likes_counter = 0
        self.comments = []

    def add_like(self):
        self.likes_counter += 1

    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        desc_font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        ui_font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
        screen.blit(desc_font.render(self.description, True, BLACK), [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS])
        screen.blit(ui_font.render(self.location, True, LIGHT_GRAY), [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS])
        screen.blit(ui_font.render(f"liked by {self.likes_counter} users", True, BLACK), [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS])
        self.display_comments()

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments", True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS, VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_comment(self, text):
        self.comments.append(Comment.Comment(text))
