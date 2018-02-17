import pygame
#
from const import *
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, 5*height/6)
        self.acx = 0
        self.acy = 0
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.movement()

    def movement(self):
        self.acx = 0
        self.acy = 0
        keystate = pygame.key.get_pressed() #List of keys pressed
        # Acceleration
        if keystate[pygame.K_LEFT]:
            self.acx = -1
        if keystate[pygame.K_RIGHT]:
            self.acx = 1
        if keystate[pygame.K_UP]:
            self.acy = -1
        if keystate[pygame.K_DOWN]:
            self.acy = 1

        #Player position adjust
        self.speedx += self.acx
        self.speedy += self.acy
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #Edge block
        if self.rect.right >= width:
            self.acx = 0
            self.speedx = 0
            self.rect.right = width - 1
        if self.rect.left <= 0:
            self.acx = 0
            self.speedx = 0
            self.rect.left = 1
        if self.rect.top <= 0:
            self.acy = 0
            self.speedy = 0
            self.rect.top = 1
        if self.rect.bottom >= height:
            self.acy = 0
            self.speedy = 0
            self.rect.bottom = height - 1
