import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, isMyPlayer=False, network_sender=None):
        super().__init__()
        self.image = pygame.image.load('assets/IcyTower.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(midbottom=(100, 400))
        self.prevX = self.rect.x
        self.PrevY = self.rect.y
        self.gravity = 0
        self.speed = 5
        self.isMyPlayer = isMyPlayer
        self.network_sender = network_sender

    def player_input(self, walls):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.left = wall.rect.right 
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect.right = wall.rect.left 
        if keys[pygame.K_SPACE] and self.gravity == 0:
            self.gravity = -20

    def updatePosToSocket(self):
        # Only send if position has actually changed
        if self.prevX == self.rect.x and self.PrevY == self.rect.y:
            return
        
        self.PrevY = self.rect.y  
        self.prevX = self.rect.x

        if self.network_sender:
            pos_data = {"x": self.rect.x, "y": self.rect.y}
            self.network_sender(pos_data)

    def apply_gravity(self, floors, platforms):
        self.gravity += 1
        self.rect.y += self.gravity

        for floor in floors:
            if self.rect.colliderect(floor.rect):
                if self.gravity > 0 and self.rect.bottom - self.gravity <= floor.rect.top:
                    self.rect.bottom = floor.rect.top
                    self.gravity = 0

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.gravity > 0 and self.rect.bottom - self.gravity <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.gravity = 0

    def update(self, floors, walls, platforms):
        if self.isMyPlayer:
            self.player_input(walls)
            self.apply_gravity(floors, platforms)
            self.updatePosToSocket()

    def updatePos(self,PosX,PosY):
        self.rect.x = PosX
        self.rect.y = PosY

    def getX(self):
        return self.rect.x
    def getY(self):
        return self.rect.y