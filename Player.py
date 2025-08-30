import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/IcyTower.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(midbottom=(100, 400))

        self.gravity = 0
        self.speed = 5

    def player_input(self, walls):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.left = wall.rect.right  # חוסם מעבר שמאלה
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.right = wall.rect.left  # חוסם מעבר ימינה
        if keys[pygame.K_SPACE] and self.gravity == 0:
            self.gravity = -20

    def apply_gravity(self, floors, platforms):
        self.gravity += 1
        self.rect.y += self.gravity

        # בדיקת קוליז׳ן עם הרצפה
        for floor in floors:
            if self.rect.colliderect(floor.rect):
                if self.gravity > 0 and self.rect.bottom - self.gravity <= floor.rect.top:
                    self.rect.bottom = floor.rect.top
                    self.gravity = 0

        # בדיקת קוליז׳ן עם פלטפורמות
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.gravity > 0 and self.rect.bottom - self.gravity <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.gravity = 0

    def update(self, floors, walls, platforms):
        self.player_input(walls)
        self.apply_gravity(floors, platforms)
