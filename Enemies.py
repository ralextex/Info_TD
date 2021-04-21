import pygame
import math
import os

class Enemy():
    def __init__(self,x,y,path):
        """
        Variablen
        :param : spawn ort X, spawn ort Y, Weg
        :return: None
        """
        self.alive = True
        self.size = 100
        self.speed = 5
        self.img = pygame.image.load("sprites/schwarz.png")
        self.path = path
        self.path_seg = 0
        self.x = x
        self.y = y
        self.value = 10

    def display(self, screen):
        """
        Zeigt die Enemies an
        :param screen: surface
        :return: None
        """
        self.img = pygame.transform.scale(self.img, (self.size, self.size))
        screen.blit(self.img, ((self.x - self.img.get_width()/2), (self.y - self.img.get_height()/2 )))

    def move(self):
        """
        Move enemy
        :return: None
        """
        #Geht in X Richtung
        dir_x = self.path[self.path_seg][0] - self.x
        if(dir_x < 0):
            self.x -= self.speed
        elif (dir_x > 0):
            self.x += self.speed
            
        #Geht in Y Richtung
        dir_y = self.path[self.path_seg][1] - self.y
        if(dir_y < 0):
            self.y -= self.speed
        elif (dir_y > 0):
            self.y += self.speed
        
        if(self.reached()):
            self.x = self.path[self.path_seg-1][0]
            self.y = self.path[self.path_seg-1][1]

    def reached(self):
        """
        Sagt ob das Enemy zu Ziel gekommen ist
        :return: bool
        """
        if (abs(self.path[self.path_seg][0] - self.x)<self.speed and abs(self.path[self.path_seg][1] - self.y)<self.speed):
            self.path_seg += 1
            if(self.path_seg >= len(self.path)):
                self.alive = False
            return True
        else:
            return False