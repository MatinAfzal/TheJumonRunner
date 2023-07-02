############################################################################
# TheJummonRunner Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

import pygame
from random import choice

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/07/2'

class Matin():
    """
    A class for creating and controlling Matin values
    """

    def __init__(self, settings, screen) -> None:

        self.settings = settings
        self.screen = screen

        # Specify the initial values ​​of matin
        self.matin_length = self.settings.matin_xpixels_separator
        self.matin_width = self.settings.matin_ypixels_separator
        self.matin_speed = settings.matin_speed
        self.matin_xsize = 62
        self.matin_ysize = 75
        self.frame_nums = [0, 1, 2]

        # getting screen rect
        self.screen_rect = self.screen.get_rect()

        # Load the Matin image and get its rect
        self.matin_img = pygame.image.load(self.settings.matin_animation_img).convert_alpha()
        # self.matin_img.set_colorkey(settings.WHITE)

        self.frame_backward_0 = self.get_image(self.matin_img, 0, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 0, self.settings.matin_scale, self.settings.BLACK)
        self.frame_backward_1 = self.get_image(self.matin_img, 1, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 0, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels)
        self.frame_backward_2 = self.get_image(self.matin_img, 2, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 0, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels - 28)

        self.frame_right_0 = self.get_image(self.matin_img, 0, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 1, self.settings.matin_scale, self.settings.BLACK)
        self.frame_right_1 = self.get_image(self.matin_img, 1, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 1, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels)
        self.frame_right_2 = self.get_image(self.matin_img, 2, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 1, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels - 28)

        self.frame_forward_0 = self.get_image(self.matin_img, 0, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 2, self.settings.matin_scale, self.settings.BLACK)
        self.frame_forward_1 = self.get_image(self.matin_img, 1, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 2, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels)
        self.frame_forward_2 = self.get_image(self.matin_img, 2, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 2, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels - 28)

        self.frame_left_0 = self.get_image(self.matin_img, 0, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 3, self.settings.matin_scale, self.settings.BLACK)
        self.frame_left_1 = self.get_image(self.matin_img, 1, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 3, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels)
        self.frame_left_2 = self.get_image(self.matin_img, 2, self.settings.matin_xpixels_separator, self.settings.matin_ypixels_separator, 3, self.settings.matin_scale, self.settings.BLACK, self.settings.matin_extra_xpixels - 28)

        self.matin_rect = self.frame_backward_0.get_rect()
        self.realtime_frame = self.frame_backward_0

        # Specify the location of matin on the screen
        self.matin_rect.x = self.screen_rect.centerx
        self.matin_rect.y = self.screen_rect.bottom - self.matin_ysize

        # Leon matin flags
        self.matin_mv_r = False
        self.matin_mv_l = False
        self.matin_mv_u = False
        self.matin_mv_d = False


    def get_image(self, sheet, framex, width, heigth, framey, scale, colour, extra_xpixels=0):
        """
        loading Spritesheet into selected frame 
        """
        image = pygame.Surface((width, heigth)).convert()

        if extra_xpixels != 0:
            extra_xpixels += 5
            image.blit(sheet, (0, 0), ((framex * width) + extra_xpixels, (framey * heigth), width, heigth))
        else:
            image.blit(sheet, (0, 0), ((framex * width), (framey * heigth), width, heigth))

        image = pygame.transform.scale(image, (width * scale, heigth * scale))
        image.set_colorkey(colour)

        return image

    def matin_update(self):
        """
        Updating matin's actions
        """
        self.choise = choice(self.frame_nums)
        if self.matin_mv_r and self.matin_rect.x <= self.screen_rect.right - self.matin_xsize:
            self.update_frame("R", 0)
            self.matin_rect.x += self.settings.matin_speed

        elif self.matin_mv_l and self.matin_rect.x >= 0:
            self.update_frame("L", 0)
            self.matin_rect.x -= self.settings.matin_speed
        
        elif self.matin_mv_u and self.matin_rect.y >= 0:
            self.update_frame("U", 0)
            self.matin_rect.y -= self.settings.matin_speed
        
        elif self.matin_mv_d and self.matin_rect.y <= self.screen_rect.bottom - self.matin_ysize:
            self.update_frame("D", 0)
            self.matin_rect.y += self.settings.matin_speed


    def update_frame(self, direction, frame_num):
        """
        Changing the matin frame in the direction of movement
        direction: R , L , U , D
        frame_num: 1 , 2 , 3
        """

        if direction == "R":
            if frame_num == 0:
                self.realtime_frame = self.frame_right_0
            elif frame_num == 1:
                self.realtime_frame == self.frame_right_1
            elif frame_num == 2:
                self.realtime_frame == self.frame_right_2
        elif direction == "L":
            if frame_num == 0:
                self.realtime_frame = self.frame_left_0
            elif frame_num == 1:
                self.realtime_frame == self.frame_left_1
            elif frame_num == 2:
                self.realtime_frame == self.frame_left_2
        elif direction == "U":
            if frame_num == 0:
                self.realtime_frame = self.frame_forward_0
            elif frame_num == 1:
                self.realtime_frame == self.frame_forward_1
            elif frame_num == 2:
                self.realtime_frame == self.frame_forward_2
        elif direction == "D":
            if frame_num == 0:
                self.realtime_frame = self.frame_backward_0
            elif frame_num == 1:
                self.realtime_frame == self.frame_backward_1
            elif frame_num == 2:
                self.realtime_frame == self.frame_backward_2

    def bltime_matin(self):
        """
        Draw matin in current loaction
        """
        self.screen.blit(self.realtime_frame, self.matin_rect)

    def center(self):
        """
        spawn matin on center in every new game
        """
        self.matin_rect.x = self.screen_rect.centerx
        self.matin_rect.y = self.screen_rect.bottom - self.matin_ysize