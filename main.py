import pygame

from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, UI_FONT_SIZE, USER_NAME_X_POS, USER_NAME_Y_POS
from classes.ImagePost import ImagePost
from classes.TextPost import TextPost


# from classes.Button import Button


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

    # TODO: add a post here
    noa = ImagePost("Noa Kirel", "Tel Aviv, Israel", "Ani Panthera!", "Images/noa_kirel.jpg")
    ron = ImagePost("Ronaldo", "Madrid, Spain", "Here I come!!!", "Images/ronaldo.jpg")
    welcome = TextPost("Me", "Makif A", "Hello world!!!",
                       "Here I come, Nitzamim class!!! See you there ;)", (0, 200, 0), (100, 150, 255))
    posts = [noa, ron, welcome]
    posts.pop()

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        username_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        screen.blit(username_font.render("nitzan17", True, BLACK), (USER_NAME_X_POS, USER_NAME_Y_POS))
        welcome.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
