import pygame
import random
##
from const import *
from settings import *
from player import *
from mobs import *
from sprites import *

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shoothell UP")
clock = pygame.time.Clock()

#Game loop
loop = True
while loop:
    clock.tick(FPS)

    #Update
    all_sprites.update()

    #Draw
    screen.fill(BLUE)
    all_sprites.draw(screen)

    #Show on screen
    pygame.display.flip()

    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

pygame.quit()
