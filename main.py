import pygame
import sys

# --- אתחול ספריית pygame ---
pygame.init()

# --- יצירת חלון ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("המשחק שלי")

# --- משתנה לשליטה בקצב פריימים ---
clock = pygame.time.Clock()

# --- לולאת המשחק ---
running = True
while running:
    # טיפול באירועים (כמו יציאה)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ניקוי המסך בצבע שחור (RGB)
    screen.fill((0, 0, 0))

    # ציור דברים כאן...
    # pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

    # עדכון המסך
    pygame.display.flip()

    # הגבלת FPS ל־60
    clock.tick(60)

# --- סיום וסגירה ---
pygame.quit()
sys.exit()
