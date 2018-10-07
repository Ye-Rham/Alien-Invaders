import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen, spritesheet):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.imagerects = ((96, 432, 96, 48), (192, 384, 96, 96), (288, 384, 96, 96), (384, 384, 96, 96),
                           (0, 480, 96, 96), (96, 480, 96, 96), (192, 480, 96, 96), (288, 480, 96, 96),
                           (384, 480, 96, 96), (0, 576, 96, 96), (96, 576, 96, 96), (192, 576, 96, 96))
        self.images = spritesheet.images_at(self.imagerects, colorkey=(255, 255, 255))
        self.rect = self.images[0].get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self .screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.hit = False
        self.hitframe = 1
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.images[0], self.rect)

    def blithit(self):
        self.screen.blit(self.images[self.hitframe], self.rect)
        self.hitframe += 1
        if self.hitframe == 12:
            self.hitframe = 1
            self.hit = False

    def center_ship(self):
        self.center = self.screen_rect.centerx