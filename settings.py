############################################################################
# TheJummonRunner Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

import os

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/07/2'

class Settings():
    """
    Game Settings
    """

    def __init__(self) -> None:

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

        # Matin variables
        self.matin_speed = 4
        self.matin_scale = 2
        self.matin_extra_xpixels = 10
        self.matin_extra_ypixels = 0
        self.matin_xpixels_separator = 41 - self.matin_extra_xpixels
        self.matin_ypixels_separator = 36

        # points
        self.points = 0
        self.all_time = 0

        # Enchanted Bullets variables
        self.bullet_speed = 1
        self.bullet_spawn_rate = 1
        self.bullet_spawn_chance = 2 # per 150
        
        # Directories
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'relative/path/to/file/you/want')

        # self.matin_animation_img = r'\assets\matin.png'
        # self.bullet_sprite_img = r'\assets\enchanted_bullet.png'
        # self.save = r'\save\score_board.txt'
        # self.start_effect = r'\assets\start_effect.ogg'
        # self.end_effect = r'\assets\end_effect.ogg'
        # self.move_effect = r'\assets\move_effect.wav'
        # self.background_music = r'\assets\background_music.ogg'
        # self.screen_icon = r'\assets\enchanted_bullet.png'

        self.matin_animation_img = dirname + "\\assets\\matin.png"
        self.bullet_sprite_img = dirname + '\\assets\\enchanted_bullet.png'
        self.save = dirname + '\\save\\score_board.txt'
        self.start_effect = dirname + '\\assets\\start_effect.ogg'
        self.end_effect = dirname + '\\assets\\end_effect.ogg'
        self.move_effect = dirname + '\\assets\\move_effect.wav'
        self.background_music = dirname + '\\assets\\background_music.ogg'
        self.screen_icon = dirname + '\\assets\\enchanted_bullet.png'

        # Display Variables
        self.screen_width = 1000
        self.screen_height =  1000
        self.resolotion = (self.screen_width, self.screen_height)
        self.FPS = 60

        self.screen_color = self.BLACK

        # Main flags
        self.run = True
        self.active = False

        # Texts
        self.caption = "The Jumon Runer"
        self.about_me = "Created by Matin Afzal:"
        
        # Url's
        self.github_url = "https://github.com/MatinAfzal/TheJumonRunner"

    def reset(self):
        self.points = 0
