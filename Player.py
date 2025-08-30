import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/IcyTower.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(
            midbottom=(100, 100))  # מתחיל גבוה יותר

        # פיזיקה
        self.gravity = 0
        self.speed = 5

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # קפיצה
        if keys[pygame.K_SPACE] and self.gravity == 0:  # רק אם עומד
            self.gravity = -20

    def apply_gravity(self, floors):
        self.gravity += 1
        self.rect.y += self.gravity

        # בדיקת קוליז׳ן עם הפלטפורמות
        for floor in floors:
            if self.rect.colliderect(floor.rect):
                # רק אם נופל מלמעלה
                if self.gravity > 0 and self.rect.bottom - self.gravity <= floor.rect.top:
                    self.rect.bottom = floor.rect.top
                    self.gravity = 0

    def update(self, floors):
        self.player_input()
        self.apply_gravity(floors)
