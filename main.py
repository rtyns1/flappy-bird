import pygame
from settings import *
from gameplay.bird import*
from gameplay.obstacles import Pipe

pygame.init()

screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Flappy Birds")
clock = pygame.time.Clock()
bird = Bird()
pipe = Pipe(GAME_WIDTH)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird.update()
    pipe.update()
    screen.fill(SKY_BLUE)
    pipe.draw(screen)
    bird.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()