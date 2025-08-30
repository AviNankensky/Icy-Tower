import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/IcyTower.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # מתאים גודל
        self.rect = self.image.get_rect(midbottom=(100, 300))

        # פיזיקה
        self.gravity = 0
        self.speed = 5

        # סאונד קפיצה
        # self.jump_sound = pygame.mixer.Sound('audio/jump_sound1.mp3')

    def player_input(self):
        keys = pygame.key.get_pressed()
        # תנועה שמאלה/ימינה
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # קפיצה
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            # self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:  # רצפה
            self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
