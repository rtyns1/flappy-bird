import pygame
import argparse
from settings import *
from gameplay.bird import *
from gameplay.obstacles import Pipe
from Bridge.keyboard import KeyboardController
from Bridge.gesture import GestureController

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Flappy Birds")
clock = pygame.time.Clock()

# Choose controller
parser = argparse.ArgumentParser()
parser.add_argument('--control', choices=['keyboard', 'gesture'], default='keyboard')
args = parser.parse_args()

if args.control == 'gesture':
    controller = GestureController()
    print("Gesture control mode - wave hand up to flap")
else:
    controller = KeyboardController()
    print("Keyboard control mode - press SPACE to flap")

# Game variables
bird = Bird()
pipes = []
score = 0
spawn_timer = 0
game_state = "MENU"  # MENU, PLAYING, GAME_OVER

# Fonts
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 40)


def check_collisions():
    if bird.rect.top <= 0 or bird.rect.bottom >= GAME_HEIGHT:
        return True
    for pipe in pipes:
        if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
            return True
    return False


def reset_game():
    global bird, pipes, score, spawn_timer, game_state
    bird = Bird()
    pipes = []
    score = 0
    spawn_timer = 0
    game_state = "PLAYING"


# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000.0  # Delta time in seconds

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update controller (reads camera if in gesture mode)
    controller.update(dt)

    # Game state machine
    if game_state == "MENU":
        if controller.should_start():
            reset_game()

    elif game_state == "PLAYING":
        # Flap from controller
        if controller.should_flap():
            bird.flap()

        bird.update()

        # Spawn pipes
        spawn_timer += 1
        if spawn_timer > 90:
            pipes.append(Pipe(GAME_WIDTH))
            spawn_timer = 0

        # Update pipes and score
        for pipe in pipes[:]:
            pipe.update()
            if not pipe.passed and pipe.x + PIPE_WIDTH < bird.rect.x:
                pipe.passed = True
                score += 1
            if pipe.offscreen():
                pipes.remove(pipe)

        # Check collisions
        if check_collisions():
            game_state = "GAME_OVER"

    elif game_state == "GAME_OVER":
        if controller.should_start():
            reset_game()

    # Draw everything
    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, GROUND_BROWN, (0, GAME_HEIGHT - 50, GAME_WIDTH, 50))

    for pipe in pipes:
        pygame.draw.rect(screen, PIPE_GREEN, pipe.top_rect)
        pygame.draw.rect(screen, PIPE_GREEN, pipe.bottom_rect)

    pygame.draw.rect(screen, BIRD_YELLOW, bird.rect)

    score_text = font.render(str(score), True, WHITE)
    screen.blit(score_text, (GAME_WIDTH // 2 - 20, 50))

    if game_state == "MENU":
        text = small_font.render("PRESS SPACE TO START", True, WHITE)
        screen.blit(text, (GAME_WIDTH // 2 - text.get_width() // 2, GAME_HEIGHT // 2))
    elif game_state == "GAME_OVER":
        text = small_font.render(f"SCORE: {score}", True, WHITE)
        screen.blit(text, (GAME_WIDTH // 2 - text.get_width() // 2, GAME_HEIGHT // 2))
        text2 = small_font.render("PRESS SPACE TO RESTART", True, WHITE)
        screen.blit(text2, (GAME_WIDTH // 2 - text2.get_width() // 2, GAME_HEIGHT // 2 + 50))

    pygame.display.flip()

pygame.quit()