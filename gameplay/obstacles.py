import pygame
from settings import *
import random


class Pipe:
    def __init__(self, x):
        min_gap = 100
        max_gap = GAME_HEIGHT - PIPE_GAP - 100
        self.gap_y = random.randint(min_gap, max_gap)
        self.top_rect = pygame.Rect(x, 0, PIPE_WIDTH, self.gap_y)
        self.bottom_y = self.gap_y + PIPE_GAP
        self.bottom_rect = pygame.Rect(x, self.gap_y + PIPE_GAP,PIPE_WIDTH, GAME_HEIGHT - self.bottom_y)

        self.passed = False


    def update(self):
        self.top_rect.x -= PIPE_SPEED
        self.bottom_rect.x -= PIPE_SPEED


    def draw(self, screen):
        pygame.draw.rect(screen, PIPE_GREEN, self.top_rect)
        pygame.draw.rect(screen, PIPE_GREEN, self.bottom_rect)



    def offscreen(self):
        return self.top_rect.x + PIPE_WIDTH< 0
