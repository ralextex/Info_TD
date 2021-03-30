
# Importieren der Pygame-Bibliothek
from pygame import *
import random
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


        self.Enemy=Enemy()
        self.health = 100
        self.money = 10000
        self.towers = []
        self.enemies = [Rot()]
        self.positions = []
        self.background = pygame.image.load("Sprites\Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(self.displayWeite,self.displayHöhe))
        
    def start(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.screen.blit(self.background,(0,0))
            self.Enemy.draw(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    run = False
            #durch gegener Loopen
            delEnemies = []

            for en in self.enemies:
                en.move()
                if en.x < self.displayWeite :
                    delEnemies.append(en)
                else:
                    en.draw(self.screen)

            #alle gegner nihct im screen löschen
            for d in delEnemies:
                self.enemies.remove(d)

        pygame.quit()

Spiel = TDgui()
Spiel.start()