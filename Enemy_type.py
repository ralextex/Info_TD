import pygame
from Enemies import Enemy
class Rot(Enemy):
    def __init__(self):
        Enemy.__init__(self)

        self.img = pygame.image.load("sprites/rot.png")

