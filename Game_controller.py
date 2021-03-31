# Importieren der Pygame-Bibliothek
import pygame 
from random import randint
import os

from Enemy_controller import *
"""
pygame.transform.scale(width,height)
um die größe von den bildern zu ändern
"""

# un commentaire 


class Game_controller(Enemy_controller):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arcade", 80)
        pygame.display.set_caption("tower defense")
        self.displayWeite,self.displayHöhe = 1000,600
        self.screen = pygame.display.set_mode((self.displayWeite, self.displayHöhe))

        self.clk = 0

        self.en_crtl = Enemy_controller(self.screen)

        
        self.health = 100
        self.money = 1000
        self.round = 1
        self.round_alive = 1

        self.background = pygame.image.load("sprites/Hintergrund.png")
        self.background = pygame.transform.scale(self.background,(800,self.displayHöhe))

        self.health_text = self.font.render(("Lives: %d" % self.health), False,(0, 0, 0) )
        self.money_text = self.font.render(("Money: %d" % self.money), False,(0, 0, 0) )
        self.round_text = self.font.render(("Round: %d" % self.round), False,(0, 0, 0) )


    def display_static(self):
        self.screen.blit(self.background,(0,0))
        display_grid(self.screen, 10)
        pygame.draw.rect(self.screen, (0, 0, 0), (630, 500, 160, 90))
        self.screen.blit(self.health_text,(0,0))
        self.screen.blit(self.money_text, (0,100))
        self.screen.blit(self.round_text, (0,200))

    def event_handler(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                pygame.quit()
            #debug purpose only
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def start(self):
        run = True
        nb_en = 0
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)
            self.event_handler()

            self.clk = 0
            # self.round_alive = 1

            nb_en = self.round * 5

            while (self.round_alive):
                self.display_static()
                self.event_handler()

                self.en_crtl.spawn(self.clk,nb_en,10)
                
                en_state = self.en_crtl.check_enemies()
                if(en_state == -1):
                    self.round_alive = 0
                    print("ROUND IS FINISHED")
                else:
                    self.health -= en_state
                    self.health_text = self.font.render(("Lives: %d" % self.health), False,(0, 0, 0) )

                self.clk += 1
                pygame.display.update()

            self.round += 1
            self.round_text = self.font.render(("Round: %d" % self.round), False,(0, 0, 0) )

def display_grid(screen, res):
    x = [i for i in range(screen.get_width()) if (i % res == 0)]
    for i in x:
        pygame.draw.line(screen,(255,255,255),(i,0),(i,screen.get_height()),1)

    y = [i for i in range(screen.get_height()) if (i % res == 0)]
    for j in y:
        pygame.draw.line(screen,(255,255,255),(0,j),(screen.get_width(),j),1)

