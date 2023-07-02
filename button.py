############################################################################
# TheJummonRunner Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

from pygame import Rect, font

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/07/2'

class Button():

    def __init__(self, settings, screen, msg, gitthub=False):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 225, 0)
        self.text_color = (255, 255, 255)
        self.font = font.SysFont(None, 48)

        # Build the button's rect object and center it.
        
        if gitthub:
            self.rect = Rect(0, 0, 120, 50)
            self.rect.center = (260, 955)
            self.font = font.SysFont(None, 30)
        else:
            self.rect = Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center

        # The button massage needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into  a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw massage.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
