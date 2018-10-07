import pygame.font
from pygame.transform import scale


class Title:
    def __init__(self, screen, msg, line, text_color):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 72)

        self.rect = pygame.Rect(0, 0, 0, 0)
        self.rect.centerx, self.rect.centery = self.screen_rect.centerx, self.screen_rect.centery/4 + line

        self.msg_image = None
        self.msg_image_rect = None

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, (0, 0, 0))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        self.screen.blit(self.msg_image, self.msg_image_rect)


class AlienPoints:
    def __init__(self, screen, spritesheet, ai_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (150, 150, 150)
        self.font = pygame.font.SysFont(None, 48)
        self.imagerects = ((0, 0, 96, 96), (0, 96, 96, 96), (0, 192, 96, 96), (0, 288, 96, 96))
        self.images = spritesheet.images_at(self.imagerects, colorkey=(255, 255, 255))
        self.rect = pygame.Rect(0, 0, 72, 72)
        self.rect.centerx, self.rect.centery = self.screen_rect.centerx, self.screen_rect.centery - 96

        self.msg_image1 = None
        self.msg_image1_rect = None
        self.msg_image2 = None
        self.msg_image2_rect = None
        self.msg_image3 = None
        self.msg_image3_rect = None
        self.msg_image4 = None
        self.msg_image4_rect = None
        self.imagerect = self.rect

        self.prep_msg(ai_settings.alien1_points, ai_settings.alien2_points, ai_settings.alien3_points, "= ???")

    def prep_msg(self, msg1, msg2, msg3, msg4):
        self.msg_image1 = self.font.render("= " + str(msg1), True, self.text_color, (0, 0, 0))
        self.msg_image1_rect = self.msg_image1.get_rect()
        self.msg_image1_rect.left, self.msg_image1_rect.centery = self.rect.centerx, self.rect.centery
        self.msg_image2 = self.font.render("= " + str(msg2), True, self.text_color, (0, 0, 0))
        self.msg_image2_rect = self.msg_image2.get_rect()
        self.msg_image2_rect.left, self.msg_image2_rect.centery = self.rect.centerx, self.msg_image1_rect.centery + 72
        self.msg_image3 = self.font.render("= " + str(msg3), True, self.text_color, (0, 0, 0))
        self.msg_image3_rect = self.msg_image3.get_rect()
        self.msg_image3_rect.left, self.msg_image3_rect.centery = self.rect.centerx, self.msg_image2_rect.centery + 72
        self.msg_image4 = self.font.render(msg4, True, self.text_color, (0, 0, 0))
        self.msg_image4_rect = self.msg_image4.get_rect()
        self.msg_image4_rect.left, self.msg_image4_rect.centery = self.rect.centerx, self.msg_image3_rect.centery + 72

    def draw(self):
        self.screen.blit(self.msg_image1, self.msg_image1_rect)
        self.imagerect.right, self.imagerect.centery = self.msg_image1_rect.left - 5, self.msg_image1_rect.centery
        self.screen.blit(scale(self.images[0], (72, 72)), self.imagerect)
        self.screen.blit(self.msg_image2, self.msg_image2_rect)
        self.imagerect.centery = self.msg_image2_rect.centery
        self.screen.blit(scale(self.images[1], (72, 72)), self.imagerect)
        self.screen.blit(self.msg_image3, self.msg_image3_rect)
        self.imagerect.centery = self.msg_image3_rect.centery
        self.screen.blit(scale(self.images[2], (72, 72)), self.imagerect)
        self.screen.blit(self.msg_image4, self.msg_image4_rect)
        self.imagerect.centery = self.msg_image4_rect.centery
        self.screen.blit(scale(self.images[3], (72, 72)), self.imagerect)
