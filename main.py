import random
import pygame
import sys
from PlatformBlock import PlatformBlock
from Player import Player
from floor import Floor
from Wall import Wall
from create_platforms import create_platforms  # הקפד להשתמש בשם הנכון

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("המשחק שלי")
clock = pygame.time.Clock()

background = pygame.image.load("assets/stoneWall.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player = pygame.sprite.GroupSingle()
player.add(Player(True))

player2In = Player(False)
player2 = pygame.sprite.GroupSingle()
player2.add(player2In)


floor = pygame.sprite.Group()
floor.add(Floor(400, 600, 800, 100))

# קירות צדדיים
walls = pygame.sprite.Group()
walls.add(Wall(0, HEIGHT, HEIGHT))      
walls.add(Wall(WIDTH, HEIGHT, HEIGHT))  

# יצירת פלטפורמות רנדומליות
platformBlocks = create_platforms(num_platforms=10, width=100, height=20, screen_width=WIDTH, screen_height=HEIGHT)

def onRun():
    if player.sprite.rect.top < HEIGHT // 3:
        scroll_amount = HEIGHT // 3 - player.sprite.rect.top
        player.sprite.rect.top = HEIGHT // 3

        # להזיז את כל הפלטפורמות
        for platform in platformBlocks:
            platform.rect.y += scroll_amount
        for floor_block in floor:
            floor_block.rect.y += scroll_amount

        for platform in list(platformBlocks):
            if platform.rect.top > HEIGHT + 50:  # אם ירדה מתחת למסך
                platformBlocks.remove(platform)   # הסרה
                # יצירת פלטפורמה חדשה למעלה
                new_x = random.randint(50, WIDTH - 50)
                new_y = random.randint(-100, -20)  # מעל המסך
                platformBlocks.add(PlatformBlock(new_x, new_y))

def updatePlayer2(x , y):
    player2In.updatePos(x,y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    floor.draw(screen)
    walls.draw(screen)
    platformBlocks.draw(screen)

    player.update(floor, walls, platformBlocks)
    player.draw(screen)

    # example of player 2
    player2.draw(screen)
    # player2In.updatePos(player2In.getX(),player2In.getY() - 1)

    onRun()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
