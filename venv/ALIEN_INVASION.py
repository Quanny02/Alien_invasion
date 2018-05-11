import sys

import pygame

def run_gam():
    #initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode ((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #start the main loop for the game
    while true:

        # watch for keyboard and mouse events.
        for events in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.EXIT()

        #make the most recently drawn screen visible
        pygame.display.flip()

--snip--
def run_game():
    --snip--
    pygame.display.set_caption("Alien Invasion")

    #set the background color
    bg_color = (250, 240, 230)

    #start the main loop for the game
    while true:

        #watch for the keyboard and mouse events.
        --snip--

        #redraw the screen during eacj pass through the loop
        screen.fill(bg_color)

        #make the most recently drawn screen visible
        pygame.display.flip


        run_game()

