import pygame

# ====== מחלקת Floor (פלטפורמה) ======
class Floor(pygame.sprite.Sprite):
    def __init__(self, x=100, y=300, width=60, height=60, color=(200, 200, 200)):
        super().__init__()
        # ניצור משטח (Surface) ריק ונצייר עליו מלבן
        self.image = pygame.Surface((width, height))
        self.image.fill(color)  # נצבע אותו בצבע אחיד (אפור בהיר לדוגמה)

        # נגדיר את המיקום שלו
        self.rect = self.image.get_rect(midbottom=(x, y))
