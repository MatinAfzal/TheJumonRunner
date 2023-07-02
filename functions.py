############################################################################
# TheJummonRunner Created By Matin Afzal
# https://github.com/MatinAfzal
# contact.matin@yahoo.com
############################################################################

import pygame as pg
import settings
import enchantedbullets
import sys
import json
from random import randint
from time import time, sleep
from webbrowser import open_new_tab

# File identity information
__author__ = 'Matin Afzal (contact.matin@yahoo.com)'
__version__ = '0.0.1'
__last_modification__ = '2023/07/2'

# Assign class and variables
set = settings.Settings()
start_time = 0 # global variable for check_play_button() function
all_time_score_rect = pg.Rect(10, 10, 30, 30)
pg.mixer.init()
pg.mixer.music.load(set.background_music)

def check_event(event, matin_rect, bullets, button, matin, github_button):
    """
    Checking input from mouse and keyboard
    """

    if event.type == pg.QUIT:
        set.run = False
        sys.exit()
    
    elif event.type == pg.KEYDOWN:
        # update bullets move 2 time in each loop when moving
        for bullet in bullets:
            bullet.move_towards_matin(matin_rect)
            check_bullet_matin_collisions(bullet, bullets, matin_rect)

        if event.key == pg.K_RIGHT:
            matin_rect.matin_mv_r = True
        elif event.key == pg.K_LEFT:
            matin_rect.matin_mv_l = True
        elif event.key == pg.K_UP:
            matin_rect.matin_mv_u = True
        elif event.key == pg.K_DOWN:
            matin_rect.matin_mv_d = True
    
    elif event.type == pg.KEYUP:
        if event.key == pg.K_RIGHT:
            matin_rect.matin_mv_r = False
        elif event.key == pg.K_LEFT:
            matin_rect.matin_mv_l = False
        elif event.key == pg.K_UP:
            matin_rect.matin_mv_u = False
        elif event.key == pg.K_DOWN:
            matin_rect.matin_mv_d = False
    
    elif event.type == pg.MOUSEBUTTONDOWN:
        mouse_x , mouse_y = pg.mouse.get_pos()
        check_play_button(button, mouse_x, mouse_y, matin, bullets)
        check_github_button(github_button, mouse_x, mouse_y)
    
def screen_background(screen, color):
    """
    set screen background
    """

    screen.fill(color)

def screen_draw(clock, screen, matin_rect, bullets, text_box, font, button, github_button):
    """
    Drawing everithing on screen
    """

    if not set.active:
        button.draw_button()
        github_button.draw_button()
        pg.draw.rect(screen, set.BLACK, all_time_score_rect, 30), 

        draw_text(font, screen, all_time_score_rect.center,
                   "Best score: " + update_scoreboard(True) # update all time
                )
        
        about_me = font.render(set.about_me, True, set.WHITE)
        screen.blit(about_me, (10, set.resolotion[1] - 50))

    else:

        clock.tick(set.FPS)

        matin_rect.matin_update()
        matin_rect.bltime_matin()

        spawn_bullets(screen, bullets)
        bullets.update()
        bullets.draw(screen)

        for bullet in bullets:
            bullet.move_towards_matin(matin_rect)
            check_bullet_matin_collisions(bullet, bullets, matin_rect)

    pg.draw.rect(screen, set.BLACK, text_box, 30), draw_text(font, screen, text_box.center, set.points)
    update_point()

def bullet_spawning_pos(resolotion) -> tuple:
        # Generate random position for spawning bullets out of resolotion
        random_x_1 = randint(resolotion[0] + 100, resolotion[0] + 500)
        
        random_y_1 = randint(resolotion[1] + 100, resolotion[1] + 500)
        
        x = random_x_1
        y = random_y_1
        
        bullet_pos = (x, y)
        return bullet_pos

def create_bullet(screen, bullets):
    """
    Create bullet in random position
    """

    bullet = enchantedbullets.EnchantedBullet(set, screen)
    bullet_pos = bullet_spawning_pos(set.resolotion)
    bullet.rect.centerx = bullet_pos[0]
    bullet.rect.centery = bullet_pos[1]
    bullets.add(bullet)
    

def spawn_bullets(screen, bullets):
    """
    spawning bullets
    """
    
    if randint(0,150) < set.bullet_spawn_chance:
        create_bullet(screen, bullets)

def check_bullet_matin_collisions(bullet, bullets, matin):
    if matin.matin_rect.colliderect(bullet):
        play_soundeffect(set.end_effect)
        sleep(1.1)
        bullets.remove(bullet)
        game_over()

def draw_text(font, screen, pos, msg):
    """
    render record (points) text
    """
    img = font.render(str(msg), True, set.GREEN)
    screen.blit(img, pos)

    return img


def game_over():
    """
    game over
    """
    
    set.active = False
    update_scoreboard() # update all time
    set.reset() # reset temp points
    pg.mixer.music.stop()
    pg.mouse.set_visible(True)

def update_point():
    """
    update points in every seconds
    """
    if set.active:
        set.points = round(time() - start_time, 1)

def check_play_button(button, mouse_x, mouse_y, matin, bullets):
    """
    start new game when the player clicks play
    """

    global start_time

    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)

    if (button_clicked) and not set.active:
        
        play_soundeffect(set.start_effect) # play starting sound
        pg.mixer.music.play(-1, 0, 1)

        pg.mouse.set_visible(False)
        set.reset()
        set.active = True

        bullets.empty()
        matin.center()

        start_time = time()

def update_scoreboard(score=False):
    """
    save all time high score in json file
    return: and returns high score
    """

    if set.points > set.all_time:
        with open(set.save, "w") as f:
            f.write(str(set.points))
    
    try:
        with open(set.save) as f:
            set.all_time = json.load(f)
    except json.JSONDecodeError:
        set.all_time = 0

    if score:
        return str(set.all_time)
    
def play_soundeffect(sound_address, time=0, volume=0, fade=0):
    """
    play given sound
    """

    effect = pg.mixer.Sound(sound_address)
    pg.mixer.Sound.play(effect, time, fade)
    pg.mixer.music.stop()

def check_github_button(github_button, mouse_x, mouse_y):
    """
    open github page when player clicks on My Github Button
    """

    github_button_clicked = github_button.rect.collidepoint(mouse_x, mouse_y)

    if github_button_clicked:
        open_new_tab(set.github_url)