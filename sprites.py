import pygame
#
from const import *
from settings import *
from player import *
from mobs import *

all_sprites = pygame.sprite.Group()
#Player sprites
player = Player()
all_sprites.add(player)
#Mob sprites
mob = Mob()
mob_sprites = pygame.sprite.Group()
mob_sprites.add(mob)
all_sprites.add(mob)
