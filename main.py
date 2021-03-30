
# Importieren der Pygame-Bibliothek
import pygame
import random
import os

import Enemies
from enemy_sprites import Rot
"""
pygame.transform.scale(width,height)
um die größe von den bildern zu ändern
"""



class TDgui():
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("tower defense")
        self.displayWeite,self.displayHöhe = 800,600
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))



        self.health = 100
        self.money = 10000
        self.towers = []
        self.enemies = [Rot()]
        self.positions = []
        self.background = pygame.image.load("Sprites/Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(self.displayWeite,self.displayHöhe))
    def start(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.screen.blit(self.background,(0,0))
            self.movementtest.draw(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    run = False

                position = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.positions.append(position)
                    print(self.positions)
            #durch gegener Loopen
            delEnemies = []
            for en in self.enemies:
                if en.x < self.displayWeite +10:
                    delEnemies.append(en)

            #alle gegner nihct im screen löschen
            for d in delEnemies:
                self.enemies.remove(d)

            self.draw

        pygame.quit()

Spiel = TDgui()
Spiel.start()