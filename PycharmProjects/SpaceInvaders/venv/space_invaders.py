import pygame
from pygame.sprite import Group
import random

from settings import Settings
from start_screen import Title
from start_screen import AlienPoints
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien1
from alien import Alien2
from alien import Alien3
from alien import Alien4
from sprite_sheet import SpriteSheet
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invaders")
    spritesheet = SpriteSheet('Spritesheet.png', screen)
    title1 = Title(screen, "SPACE", 0, (200, 200, 200))
    title2 = Title(screen, "INVADERS", 50, (20, 200, 20))
    title3 = Title(screen, "HIGH SCORES", 0, (200, 200, 200))
    alienpoints = AlienPoints(screen, spritesheet, ai_settings)

    play_button = Button(ai_settings, screen, "Play", ai_settings.screen_height * 0.75)
    high_score_button = Button(ai_settings, screen, "High Scores", ai_settings.screen_height * 0.85)
    back_button = Button(ai_settings, screen, "Back", ai_settings.screen_height * 0.85)

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, spritesheet)

    ship = Ship(ai_settings, screen, spritesheet)
    bullets = Group()
    alienbullets = Group()
    aliens1 = Group()
    aliens2 = Group()
    aliens3 = Group()
    alien4 = Alien4(ai_settings, screen, spritesheet)

    gf.create_fleet(ai_settings, screen, ship, aliens1, aliens2, aliens3, spritesheet)

    while True:
        timer = pygame.time.Clock()
        timer.tick(60)
        gf.check_events(ai_settings, screen, stats, sb, play_button, high_score_button, ship, aliens1, aliens2, aliens3,
                        bullets, alienbullets, spritesheet)

        if stats.game_active:
            if not alien4.active:
                if pygame.time.get_ticks() % 10 == 0:
                    if random.randint(1, 200) == 100:
                        alien4.active = True
                        alien4.blitme()

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets,
                              alienbullets, spritesheet)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets,
                             alienbullets, spritesheet)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens1, aliens2, aliens3, alien4, bullets, alienbullets,
                         play_button, high_score_button, back_button, title1, title2, title3, alienpoints)


run_game()
