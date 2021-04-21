import pygame
import os
import math

from Rect import *

class Tower():
    def __init__(self,x,y):
        """
        :param: X-Koordinate, Y-Koordinate
        """
        self.x = x #pos X
        self.y = y # pos Y

        # Sprite
        self.img = pygame.image.load("sprites/tower.png")
        self.width = 16
        self.height = 16
        self.size = 32
        
        # Einstellungen des Towers
        self.range = 150 # Reichweite der schusse
        self.cd = 10 # Zeit bevor neuer Schuss (Cooldown)
        self.prev = 0 # last time shot
        self.damage = 10 # Schaden

        # Hitbox
        self.space = 14 # Freiraum zwischen sprite und nachst mogliche pos
        self.hitbox = Rect(self.x-self.width-self.space, self.y-self.height-self.space, self.x+self.width+self.space, self.y+self.height+self.space)

        # Display Einstellungen
        self.disp_mode = 0 # for highlight
        self.radius_color = (0,0,255, 100)

    def draw(self, screen):
        """
        Anzeige der Tower
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
        Zeichnet den range radius
        :param : screen
        :return: None
        """
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, self.radius_color, (self.range, self.range), self.range, 0)

        screen.blit(surface, (self.x - self.range, self.y - self.range))

    def target(self, clk, screen, enemies):
        """
        Findet den nächst möglichen Gegner und fuegt Schaden zu
        :param : Clock, Screen, list of enemies
        :return: Money gained
        """
        money = 0
        target = [] # Moegliche Ziele

        # Sort enemies by proximity
        for en in enemies:
            dis = math.sqrt((self.x-en.x)**2+(self.y-en.y)**2)
            if(dis < self.range):
                target.append((en,dis))
        target.sort(key=lambda a: a[1])

        # if target exists
        if(len(target)>0):
            if(clk - self.prev > self.cd): # not on cooldown
                self.prev = clk
                pygame.draw.line(screen,(255,255,255),(self.x,self.y),(target[0][0].x, target[0][0].y),7) # Laser Beam
                
                index = enemies.index(target[0][0])
                enemies[index].health -= self.damage
                if(enemies[index].health<=0):
                    money += enemies[index].value
                    enemies.pop(index)
        return money
                

    def highlight(self):
        """
        Change Mode wenn Maus über den Tower
        :return: None
        :todo: possible overlap of hitbox
        """
        (mouse_x,mouse_y) = pygame.mouse.get_pos()
        if(self.hitbox.inside(mouse_x,mouse_y)):
            self.disp_mode = 1 
        else:
            self.disp_mode = 0