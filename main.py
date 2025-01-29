import pygame

from buttons import *
from classes.Filter import Filter
from classes.Heart import Heart
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, UI_FONT_SIZE, USER_NAME_X_POS, USER_NAME_Y_POS
from helpers import screen, mouse_in_button, read_comment_from_user, censor


def blit_hearts(hearts):
    for heart in hearts:
        heart.move()
        if heart.get_y() < heart.get_height():
            hearts.remove(heart)


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    purple_filter = Filter((30, 12, 121), 80)
    brown_filter = Filter((100, 30, 0), 60)
    posts = [
        ImagePost("Noa Kirel", "Tel-Aviv, Israel", "Ani Panthera!", "Images/noa_kirel.jpg", purple_filter),
        ImagePost("Ronaldo", "Madrid, Spain", "Here I come!!!", "Images/ronaldo.jpg"),
        TextPost("Me", "Makif A, Be'er-Sheva", "Hello world!!!",
                 "Here I come, Nitzamim class!!! See you there ;)", (0, 200, 0), (100, 150, 255)),
        TextPost("IceCreamLover15", "Golda Be'er-Sheva", "Good times!",
                 "Who said you can't eat ice cream five times a day? Not me!", (250, 200, 100), (255, 119, 188)),
        ImagePost("NikiTheDog", "Be'er-Sheva, Israel", "What is this weird flashy thing?", "Images/Niki.jpg"),
        ImagePost("ShelegTheCat", "Be'er-Sheva, Israel", "Alone time is the best...", "Images/Sheleg.jpg"),
        ImagePost("TotoThePuppy", "Be'er-Sheva, Israel", "Doggy life!", "Images/Toto.jpg"),
        ImagePost("IceCreamLover15", "Glida Be'er-Sheva", "More ice cream for me!", "Images/ice_cream.png",
                  brown_filter)
    ]
    current_post_num = 0
    hearts = []

    running = True
    while running:
        post = posts[current_post_num]
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_in_button(like_button, mouse_pos):
                    post.add_like()
                    hearts.append(Heart())
                elif mouse_in_button(click_post_button, mouse_pos):
                    current_post_num += 1
                    current_post_num %= len(posts)
                elif mouse_in_button(comment_button, mouse_pos):
                    comment_text = censor(read_comment_from_user())
                    post.add_comment(comment_text)
                elif mouse_in_button(view_more_comments_button, mouse_pos) and post.too_many_comments:
                    post.view_more_comments()

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        username_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        screen.blit(username_font.render("nitzan17", True, BLACK), (USER_NAME_X_POS, USER_NAME_Y_POS))
        post.display()
        blit_hearts(hearts)

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
