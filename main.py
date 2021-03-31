
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

        self.counter = 0
        self.health = 100
        self.money = 10000
        self.round = 1
        self.enemies_left = self.round * 5
        self.towers = []
        self.enemies = []
        self.positions = []
        self.background = pygame.image.load("Sprites\Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(self.displayWeite,self.displayHöhe))

    def spawn(self):
        
        if((self.counter % 10) == 0):
            if(self.enemies_left > 0):
                self.enemies_left -= 1 
                self.enemies.append(Enemy(126,4))

        self.counter += 1
        
    def start(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            self.screen.blit(self.background,(0,0))
            pygame.draw.rect(self.screen, (0, 0, 0), (630, 500, 160, 90))

            display_grid(self.screen, 10)


            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    run = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(mouse.get_pos())   
                

            self.spawn()

            for en in self.enemies:
                if(en.alive):
                    en.move()
                    en.display(self.screen)
                else:
                    self.enemies.remove(en)


            pygame.display.update()

        pygame.quit()

def display_grid(screen, res):
    x = [i for i in range(screen.get_width()) if (i % res == 0)]
    for i in x:
        pygame.draw.line(screen,(255,255,255),(i,0),(i,screen.get_height()),2)

    y = [i for i in range(screen.get_height()) if (i % res == 0)]
    for j in y:
        pygame.draw.line(screen,(255,255,255),(0,j),(screen.get_width(),j),2)

Spiel = TDgui()
Spiel.start()

