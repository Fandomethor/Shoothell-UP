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
        self.acX = 0
        self.acY = 0
        self.velX = 0
        self.velY = 0

    def update(self):
        self.movement_control()
        self.friction()
        self.position_change()

    def movement_control(self):
        self.acX = 0
        self.acY = 0
        keystate = pygame.key.get_pressed() #List of keys pressed
        # Acceleration
        if keystate[pygame.K_LEFT]:
            self.acX = -1
        if keystate[pygame.K_RIGHT]:
            self.acX = 1
        if keystate[pygame.K_UP]:
            self.acY = -1
        if keystate[pygame.K_DOWN]:
            self.acY = 1

        self.velX += self.acX
        self.velY += self.acY

    def friction(self):
        print(self.velX, self.velY)
        if self.velX > 0:
            self.velX -= self.velX*0.05 + 0.2
        if self.velX < 0:
            self.velX -= self.velX*0.05 - 0.2
        if self.velY > 0:
            self.velY -= self.velY*0.05 + 0.2
        if self.velY < 0:
            self.velY -= self.velY*0.05 - 0.2
        if 0.11 > self.velX > -0.11:
            self.velX = 0
        if 0.11 > self.velY > -0.11:
            self.velY = 0

    def position_change(self):
        self.rect.x += self.velX
        self.rect.y += self.velY

        #Edge block
        if self.rect.right >= width:
            self.acX = 0
            self.velX = 0
            self.rect.right = width - 1
        if self.rect.left <= 0:
            self.acX = 0
            self.velX = 0
            self.rect.left = 1
        if self.rect.top <= 0:
            self.acY = 0
            self.velY = 0
            self.rect.top = 1
        if self.rect.bottom >= height:
            self.acY = 0
            self.velY = 0
            self.rect.bottom = height - 1
