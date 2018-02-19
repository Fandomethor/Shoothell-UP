import pygame
import random
#
from const import *
from settings import *


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = spawn_height
        self.speedY = random.randrange(1, 6)

    def update(self):
        self.rect.y += self.speedY
        if self.rect.top > height + 10:
                self.rect.x = random.randrange(width - self.rect.width)
                self.rect.y = spawn_height
                self.speedY = random.randrange(1, 6)
