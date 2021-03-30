import pygame
from Enemies import Enemy
class Rot(Enemy):
    def __init__(self):
        super(Rot, self).__init__(20,20)
        """
         self.name = "rot"
        self.special_ability = "schnell"
         self.speed = 10
        
        """

        self.image = pygame.image.load("Sprites/Rot_gegener.png")

