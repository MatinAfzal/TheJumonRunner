############################################################################
# TheJummonRunner Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

import pygame
from math import hypot

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/07/2'

class EnchantedBullet(pygame.sprite.Sprite):
    """
    A class for making and processing bullets and their location
    """

    def __init__(self, settings, screen) -> None:
        super(EnchantedBullet, self).__init__()

        # Specify the initial values ​​of bullets
        self.settings = settings
        self.screen = screen

        # Load the bullet image and set its rect attribute.
        self.image = pygame.image.load(self.settings.bullet_sprite_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (140 / 4, 95 / 4))
        self.rect = self.image.get_rect()

    def move_towards_matin(self, matin):
        """
        Find direction vactor , between bullet and matin
        Update the location of the bullet according to Matin's position
        """

        dx, dy = matin.matin_rect.x - self.rect.x, matin.matin_rect.y - self.rect.y
        dist = hypot(dx, dy)
        dx, dy = dx / dist, dy/ dist # Normalize

        # Move with this Normalized vactor twards the player
        self.rect.x += dx * self.settings.bullet_speed
        self.rect.y += dy * self.settings.bullet_speed

    def bltime_bullet(self):
        """
        Draw bullet in current loaction
        """

        self.screen.blit(self.image, self.rect)

