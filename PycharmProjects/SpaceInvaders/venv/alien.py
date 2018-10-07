import pygame
import pygame.font
from pygame.sprite import Sprite
import random

class Alien1(Sprite):
    def __init__(self, ai_settings, screen, spritesheet):
        super(Alien1, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.imageframe = 0
        self.imagerects = ((0, 0, 96, 96), (96, 0, 96, 96), (192, 0, 96, 96),
                            (288, 0, 96, 96), (384, 0, 96, 96))
        self.images = spritesheet.images_at(self.imagerects, colorkey=(255, 255, 255))
        self.rect = self.images[0].get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.images[self.imageframe], self.rect)

    def next_frame(self):
        self.imageframe += 1
        if self.imageframe == 2:
            self.imageframe = 0

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

class Alien2(Sprite):
    def __init__(self, ai_settings, screen, spritesheet):
        super(Alien2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.imageframe = 0
        self.imagerects = ((0, 96, 96, 96), (96, 96, 96, 96), (192, 96, 96, 96),
                            (288, 96, 96, 96), (384, 96, 96, 96))
        self.images = spritesheet.images_at(self.imagerects, colorkey=(255, 255, 255))
        self.rect = self.images[0].get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.images[self.imageframe], self.rect)

    def next_frame(self):
        self.imageframe += 1
        if self.imageframe == 2:
            self.imageframe = 0

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

class Alien3(Sprite):
    def __init__(self, ai_settings, screen, spritesheet):
        super(Alien3, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.imageframe = 0
        self.imagerects = ((0, 192, 96, 96), (96, 192, 96, 96), (192, 192, 96, 96),
                            (288, 192, 96, 96), (384, 192, 96, 96))
        self.images = spritesheet.images_at(self.imagerects, colorkey=(255, 255, 255))
        self.rect = self.images[0].get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.images[self.imageframe], self.rect)

    def next_frame(self):
        self.imageframe += 1
        if self.imageframe == 2:
            self.imageframe = 0

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

class Alien4(Sprite):
    def __init__(self, ai_settings, screen, spritesheet):
        super(Alien4, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 24)

        self.imageframe = 0
        self.imagerects = ((0, 288, 96, 96), (96, 288, 96, 96))
        self.images = spritesheet.images_at(self.imagerects, colorkey=(255, 255, 255))
        self.rect = self.images[0].get_rect()

        self.screen_rect = screen.get_rect()
        self.msg_rect = pygame.Rect(0, 0, 0, 0)
        self.rect.right = self.screen_rect.left
        self.rect.y = self.rect.height/4

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.oscillate = -1
        self.active = False
        self.destroyed = False
        self.msgtime = 1
        self.points = 0

    def blitme(self):
        self.screen.blit(self.images[self.imageframe], self.rect)

    def next_frame(self):
        self.imageframe += 1
        if self.imageframe == 2:
            self.imageframe = 0

    def update(self):
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
        if self.rect.x % 5 == 0:
            self.y += 2 * self.oscillate
            self.rect.y = self.y
            self.oscillate *= -1

    def destroy(self, ai_settings, stats):
        self.points = int(random.randint(8, 10) * ai_settings.score_scale * 10)
        stats.score += self.points
        self.msg_rect.center = self.rect.center
        self.x = self.screen_rect.left
        self.rect.right = self.x
        self.active = False
        self.destroyed = True

    def blitdead(self):
        self.screen.blit(self.font.render(str(self.points), True, self.text_color), self.msg_rect)
        if pygame.time.get_ticks() % 30 == 0:
            self.msgtime += 1
