import pygame
import sys
from Player import Player
from Floor import Floor
from Wall import Wall

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("המשחק שלי")
clock = pygame.time.Clock()

background = pygame.image.load("assets/stoneWall.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player = pygame.sprite.GroupSingle()
player.add(Player())

floor = pygame.sprite.Group()
floor.add(Floor(400, 600, 800, 100))

# קירות צדדיים
walls = pygame.sprite.Group()
walls.add(Wall(0, HEIGHT, HEIGHT))      # קיר שמאל
walls.add(Wall(WIDTH, HEIGHT, HEIGHT))  # קיר ימין


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    floor.draw(screen)
    walls.draw(screen)

    player.update(floor, walls)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
