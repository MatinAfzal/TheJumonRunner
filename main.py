############################################################################
# TheJummonRunner Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

import pygame as pg
import settings
import functions as fc
import matin
from button import Button

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/07/2'

# Assign Settings class
set = settings.Settings()

# Initialization of pygame
pg.init()

# Creating screen surface
screen = pg.display.set_mode(set.resolotion)
clock = pg.time.Clock()
pg.display.set_caption(set.caption)

# Assign Matin class
matin_rect = matin.Matin(set, screen)
bullets = pg.sprite.Group()
font = pg.font.Font(None, 24)
text_box = pg.Rect(850, 0, 50, 50)


# define starting time
play_button = Button(set, screen, "Play")
github_button = Button(set, screen, "My Github", True)

# Load back ground music


# Main loop
def main():
    while set.run:
        for event in pg.event.get():
            fc.check_event(event, matin_rect, bullets, play_button, matin_rect, github_button)
        
        fc.screen_background(screen, set.screen_color) # fill screen background
        fc.screen_draw(clock, screen, matin_rect, bullets, text_box, font, play_button, github_button)

        pg.display.update() # update screen

    pg.quit()

if __name__ == "__main__":
    main()