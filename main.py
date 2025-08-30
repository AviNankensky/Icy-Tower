import pygame
import sys
from Player import Player

# --- אתחול pygame ---
pygame.init()

# --- יצירת חלון ---
WIDTH, HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("המשחק שלי")

clock = pygame.time.Clock()

# --- טעינת רקע ---
background = pygame.image.load("assets/stoneWall.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# --- יצירת שחקן ---
player = pygame.sprite.GroupSingle()
player.add(Player())

# --- לולאת המשחק ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ציור רקע
    screen.blit(background, (0, 0))

    # עדכון וציור שחקן
    player.update()
    player.draw(screen)

    # עדכון המסך
    pygame.display.flip()
    clock.tick(60)

# --- סיום וסגירה ---
pygame.quit()
sys.exit()
