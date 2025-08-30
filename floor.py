import pygame, sys, random
pygame.init()

# ====== מחלקת Floor (פלטפורמה) ======
class Floor:
    def __init__(self, x, y, w, h, color):
        # נשמור כ-Rect כדי להקל על ציור וקוליז׳ן
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

 