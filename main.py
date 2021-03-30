
# Importieren der Pygame-Bibliothek
from pygame import *
from random import randint
import os

from Enemies import *
from Enemy_type import Rot
"""
pygame.transform.scale(width,height)
um die größe von den bildern zu ändern
"""

# un commentaire 


class TDgui(Enemy):
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("tower defense")
        self.displayWeite,self.displayHöhe = 800,600
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))


        self.health = 100
        self.money = 10000
        self.towers = []
        self.enemies = []
        self.positions = []
        self.background = pygame.image.load("Sprites\Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(self.displayWeite,self.displayHöhe))
        
    def start(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.screen.blit(self.background,(0,0))

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    run = False
            for i in range (2):
                self.enemies.append(Enemy(randint(1,800),randint(1,600)))
            for en in self.enemies:
                if(en.alive):
                    en.move()
                    en.display(self.screen)
                else:
                    self.enemies.remove(en)


            pygame.display.update()

        pygame.quit()

Spiel = TDgui()
Spiel.start()
