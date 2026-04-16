import pygame
from settings import *

class Bird:
    def __init__(self): ##This is the constructor
        self.rect = pygame.Rect(BIRD_X, BIRD_Y, BIRD_SIZE, BIRD_SIZE)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = JUMP_STRENGTH

    def draw(self, screen):
        pygame.draw.rect(screen, BIRD_YELLOW, self.rect)
