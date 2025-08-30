import pygame

class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=20, color=(200, 200, 200)):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom=(x, y))
