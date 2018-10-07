import pygame.ftfont
from pygame.sprite import Group
from pygame.transform import scale

from ship import Ship

class Scoreboard():
    def __init__(self, ai_settings, screen, stats, spritesheet):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.spritesheet = spritesheet
        self.highscores_active = False
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 36)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render("Score: " + score_str, True, self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("High Score: " + high_score_str, True, self.text_color,
                                                 self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render("Level: " + str(self.stats.level), True, self.text_color,
                                            self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen, self.spritesheet)
            ship.images[0] = scale(ship.images[0], (48, 24))
            ship.rect.x = 10 + ship_number * ship.rect.width/2
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        for ship in self.ships:
            ship.blitme()

    def show_high_score_list(self, high_score_list, no):
        self.rect.x, self.rect.y = self.screen_rect.centerx - 60, self.screen_rect.centery/3 + 10 + no * 48
        self.screen.blit(self.font.render((str(no + 1) + ".   " + str(high_score_list[no])), True,
                                          self.text_color, (0, 0, 0)), self.rect)
