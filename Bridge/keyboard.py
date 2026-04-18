import pygame

class KeyboardController:
    def update(self, dt):

        pass

    def should_flap(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE] or keys[pygame.K_UP]

    def should_start(self):
        return self.should_flap()