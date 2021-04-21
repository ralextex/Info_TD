import pygame
import os
import math

from Rect import *

class Tower():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = pygame.image.load("sprites/tower.png")
        self.width = 16
        self.height = 16
        self.size = 32
        self.range = 150
        self.cd = 35
        self.prev = 0
        self.space = 14
        self.disp_mode = 0
        self.hitbox = Rect(self.x-self.width-self.space, self.y-self.height-self.space, self.x+self.width+self.space, self.y+self.height+self.space)
        self.price = 200

        self.radius_color = (0,0,255, 100)

    def draw(self, screen):
        """
        Zeigt die Tower an
        :param screen: surface
        :return: None
        """
        if(self.disp_mode == 0):
            self.img = pygame.transform.scale(self.img, (self.size, self.size))
            screen.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))
        else:
            self.draw_radius(screen)
            self.img = pygame.transform.scale(self.img, (self.size, self.size))
            screen.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))
    
    def draw_radius(self, screen):
        """
        Zeichnet den radius
        :param : None
        :return: None
        """
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.radius_color, (self.range, self.range), self.range, 0)

        screen.blit(surface, (self.x - self.range, self.y - self.range))

    def target(self, clk, screen, enemies):
        """
        Greift Enemies an
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        target = []

        for en in enemies:
            dis = math.sqrt((self.x-en.x)**2+(self.y-en.y)**2)
            if(dis < self.range):
                target.append((en,dis))

        target.sort(key=lambda a: a[1])

        if(len(target)>0):
            if(clk - self.prev > self.cd):
                self.prev = clk
                money += target[0][0].value
                pygame.draw.line(screen,(255,255,255),(self.x,self.y),(target[0][0].x, target[0][0].y),7)
                enemies.remove(target[0][0])
        return money
                

    def highlight(self):
        """
        Markiert den Tower wenn Maus auf den Tower
        :return: None
        """
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if(self.hitbox.inside(mouse_x,mouse_y)):
            self.disp_mode = 1
        else:
            self.disp_mode = 0