import pygame
import random
##
from const import *
from options import *
from player import *

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoothell UP")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#Game loop
loop = True
while loop:
    clock.tick(FPS)

    #Update
    all_sprites.update()

    #Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
