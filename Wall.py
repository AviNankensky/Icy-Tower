import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height, color=(150, 150, 150)):
        super().__init__()
        self.image = pygame.Surface((50, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(midbottom=(x, y))
