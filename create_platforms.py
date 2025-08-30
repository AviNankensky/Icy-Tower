import pygame
import random
from PlatformBlock import PlatformBlock

def create_platforms(num_platforms, width, height, screen_width, screen_height):
    platforms = pygame.sprite.Group()
    gap_y = screen_height // num_platforms  # מרווח גובה בין הפלטפורמות
    for i in range(num_platforms):
        x = random.randint(50, screen_width - 50)
        y = screen_height - i * gap_y
        platform = PlatformBlock(x, y, width=width, height=height)
        platforms.add(platform)
    return platforms
